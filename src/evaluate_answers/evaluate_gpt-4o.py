import os
import csv
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

INPUT_CSV = "results/raw_outputs.csv"
OUTPUT_CSV = "results/evaluations_by_LLMs/evaluation_gpt-4o.csv"
JUDGE_MODEL = "openai/gpt-4o"

with open('PROMPTS_TO_LLMs/EVALUATION_PROMPT.txt') as file:
    EVALUATION_PROMPT = file.read()


def judge_response(user_query, assistant_response):

    if not assistant_response or "ERROR" in assistant_response:
        return {
            "empathetic_accuracy": 0, "linguistic_naturalness": 0, "cultural_grounding": 0, 
            "explanation": "Skipped evaluation due to missing baseline response text."
        }
        
    content = f"[USER QUERY]: {user_query}\n[ASSISTANT RESPONSE]: {assistant_response}"

    try:
        completion = client.chat.completions.create(
            model=JUDGE_MODEL,
            messages=[
                {"role": "system", "content": EVALUATION_PROMPT},
                {"role": "user", "content": content}
            ],
            temperature=0.1, 
            timeout=25
        )
        
        raw_res = completion.choices[0].message.content.strip()
        
        if raw_res.startswith("```"):
            raw_res = raw_res.strip("```json").strip("```").strip()
            
        data = json.loads(raw_res)
        
        return {
            "empathetic_accuracy": data.get("empathetic_accuracy", 0),
            "linguistic_naturalness": data.get("linguistic_naturalness", 0),
            "cultural_grounding": data.get("cultural_grounding", 0),
            "explanation": data.get("explanation", "")
        }
    
    except Exception as e:
        return {"empathetic_accuracy": 0, "linguistic_naturalness": 0, "cultural_grounding": 0, "explanation": f"Evaluation parsing error: {str(e)}"}



def main():
    if not os.path.exists(INPUT_CSV):
        print(f"Error: Could not locate data file '{INPUT_CSV}'. Wait for generation to finish.")
        return

    fieldnames = [
        "Prompt_ID", "Category", "Tested_Model", "Language", 
        "Empathetic_Accuracy", "Linguistic_Naturalness", "Contextual_Cultural_Grounding", "Explanation"
    ]

    with open(INPUT_CSV, "r", encoding="utf-8") as infile, \
         open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as outfile:
         
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        print(f"Deployment successful. Running dataset evaluations through judge model: {JUDGE_MODEL}...")
        
        for count, row in enumerate(reader, 1):
            p_id = row["Prompt_ID"]
            cat = row["Category"]
            
            eval_segments = [
                {"model": "DeepSeek", "lang": "EN", "prompt": row["English_Prompt"], "resp": row["DeepSeek_V3_EN"]},
                {"model": "LLaMA", "lang": "EN", "prompt": row["English_Prompt"], "resp": row["LLaMA_3.3_EN"]},
                {"model": "Gemini", "lang": "EN", "prompt": row["English_Prompt"], "resp": row["Gemini_2.5_Flash_EN"]},
                {"model": "DeepSeek", "lang": "UA", "prompt": row["Ukrainian_Prompt"], "resp": row["DeepSeek_V3_UA"]},
                {"model": "LLaMA", "lang": "UA", "prompt": row["Ukrainian_Prompt"], "resp": row["LLaMA_3.3_UA"]},
                {"model": "Gemini", "lang": "UA", "prompt": row["Ukrainian_Prompt"], "resp": row["Gemini_2.5_Flash_UA"]}
            ]

            for seg in eval_segments:
                scores = judge_response(seg["prompt"], seg["resp"])
                writer.writerow({
                    "Prompt_ID": p_id,
                    "Category": cat,
                    "Tested_Model": seg["model"],
                    "Language": seg["lang"],
                    "Empathetic_Accuracy": scores["empathetic_accuracy"],
                    "Linguistic_Naturalness": scores["linguistic_naturalness"],
                    "Contextual_Cultural_Grounding": scores["cultural_grounding"],
                    "Explanation": scores["explanation"]
                })
            
            print(f"✓ [{p_id}] Category: {cat:<10} | Processed profile {count}/500")
            time.sleep(0.1)

    print(f"Evaluation pipeline processing complete. Results stored: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()