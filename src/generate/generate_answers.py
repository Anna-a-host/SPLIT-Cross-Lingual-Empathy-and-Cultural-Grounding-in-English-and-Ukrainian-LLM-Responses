import os
import csv
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


INPUT_CSV = "prompts.csv"
OUTPUT_CSV = "results/raw_outputs.csv"


MODELS = {
    "DeepSeek_V3": "deepseek/deepseek-chat",
    "LLaMA_3.3": "meta-llama/llama-3.3-70b-instruct",
    "Gemini_2.5_Flash": "google/gemini-2.5-flash"
}

with open('PROMPTS_TO_LLMs/SHORT_PROMPT_TO_ANSWER_GENERATORS.txt', encoding='utf-8') as file:
    SHORT_PROMPT_TO_ANSWER_GENERATORS = file.read()

def get_llm_response(model_id, prompt_text):
    try:
        completion = client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system", 
                    "content": SHORT_PROMPT_TO_ANSWER_GENERATORS
                },
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling {model_id}: {e}")
        return f"ERROR: {str(e)}"



def main():
    if not os.path.exists(INPUT_CSV):
        print(f"Input file not found at: {INPUT_CSV}")
        return

    # here are the output filenames
    fieldnames = [
        "Prompt_ID", "Category", 
        "English_Prompt", "DeepSeek_V3_EN", "LLaMA_3.3_EN", "Gemini_2.5_Flash_EN",
        "Ukrainian_Prompt", "DeepSeek_V3_UA", "LLaMA_3.3_UA", "Gemini_2.5_Flash_UA"
    ]

    # opening files and processing rows
    with open(INPUT_CSV, mode="r", encoding="utf-8") as infile, \
         open(OUTPUT_CSV, mode="w", encoding="utf-8", newline="") as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        print("Starting answer generation across models...")
        
        for count, row in enumerate(reader, 1):
            p_id = row["Prompt_ID"]
            category = row["Category"]
            eng_prompt = row["English_Prompt"]
            ukr_prompt = row["Ukrainian_Prompt"]

            print(f"[{count}/500] Processing ID: {p_id} ({category})...")

            # generating responses for the English baseline
            ds_en = get_llm_response(MODELS["DeepSeek_V3"], eng_prompt)
            llama_en = get_llm_response(MODELS["LLaMA_3.3"], eng_prompt)
            gemini_en = get_llm_response(MODELS["Gemini_2.5_Flash"], eng_prompt)

            # generating responses for the Ukrainian translation
            ds_ua = get_llm_response(MODELS["DeepSeek_V3"], ukr_prompt)
            llama_ua = get_llm_response(MODELS["LLaMA_3.3"], ukr_prompt)
            gemini_ua = get_llm_response(MODELS["Gemini_2.5_Flash"], ukr_prompt)

            # witing individual record immediately to prevent data loss if script stops
            writer.writerow({
                "Prompt_ID": p_id,
                "Category": category,
                "English_Prompt": eng_prompt,
                "DeepSeek_V3_EN": ds_en,
                "LLaMA_3.3_EN": llama_en,
                "Gemini_2.5_Flash_EN": gemini_en,
                "Ukrainian_Prompt": ukr_prompt,
                "DeepSeek_V3_UA": ds_ua,
                "LLaMA_3.3_UA": llama_ua,
                "Gemini_2.5_Flash_UA": gemini_ua
            })
            
            time.sleep(0.5)

    print(f"Done! Results successfully saved to: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()