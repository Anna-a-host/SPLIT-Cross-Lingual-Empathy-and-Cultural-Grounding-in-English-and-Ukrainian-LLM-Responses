import csv
import json
import os
import os.path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Reading the adjusted prompt from a separate file
with open('PROMPTS_TO_LLMs/SPLIT_500_BENCHMARK_PROMPT.txt', encoding='utf-8') as file:
    SPLIT_500_BENCHMARK_PROMPT = file.read()

# The overall process of user queries' generation following our SPLIT benchmark
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

completion = client.chat.completions.create(
    model="openai/gpt-4o",  # deploying the chosen model for queries generation
    response_format={
        "type": "json_object"
    },  # forcing the model to answer in json for a better structure
    messages=[{"role": "user", "content": SPLIT_500_BENCHMARK_PROMPT}],
)

raw_json_string = completion.choices[0].message.content
print(raw_json_string) # making sure the answer from the model is received


if raw_json_string is None:
    print("Error: The model returned an empty response.")
else:
    data = json.loads(raw_json_string) # converting the model's json response into a python dictionary
    csv_filename = "prompts.csv"


    # making sure the file exists
    file_exists = os.path.isfile(csv_filename)

    # Opening the csv file in "append" mode 
    with open(csv_filename, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                'Prompt_ID',
                'Category',
                'English_Prompt',
                'Ukrainian_Prompt',
            ],
        )

        # if this file doesn't exist yet, we write the header row first
        if not file_exists:
            writer.writeheader()

        generated_items = data.get('queries', [])
        for item in generated_items:
            writer.writerow(item)

    print(f"Prompts have been saved successfully!")