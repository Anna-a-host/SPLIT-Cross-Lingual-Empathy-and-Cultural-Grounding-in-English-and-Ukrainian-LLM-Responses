import os
import pandas as pd

INPUT_RAW_FILE = "results/raw_outputs.csv"  
OUTPUT_DIR = "human_in_the_loop_src"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "balanced_human_validation_subset.csv")

def generate_human_validation_file():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    if not os.path.exists(INPUT_RAW_FILE):
        print(f"Error: Could not find your raw file at: {INPUT_RAW_FILE}")
        return
        
    df = pd.read_csv(INPUT_RAW_FILE)
    unpacked_rows = []
    
    mapping = [
        ('DeepSeek_V3_EN', 'DeepSeek', 'EN', 'English_Prompt'),
        ('LLaMA_3.3_EN', 'LLaMA', 'EN', 'English_Prompt'),
        ('Gemini_2.5_Flash_EN', 'Gemini', 'EN', 'English_Prompt'),
        ('DeepSeek_V3_UA', 'DeepSeek', 'UA', 'Ukrainian_Prompt'),
        ('LLaMA_3.3_UA', 'LLaMA', 'UA', 'Ukrainian_Prompt'),
        ('Gemini_2.5_Flash_UA', 'Gemini', 'UA', 'Ukrainian_Prompt')
    ]
    
    for response_col, model, lang, prompt_col in mapping:
        if response_col in df.columns:
            for _, row in df.iterrows():
                unpacked_rows.append({
                    'Prompt_ID': row['Prompt_ID'],
                    'Category': row['Category'],
                    'Prompt': row[prompt_col],
                    'Tested_Model': model,
                    'Language': lang,
                    'Generated_Response': row[response_col]
                })
                
            
    vertical_df = pd.DataFrame(unpacked_rows)
    
    sampled_chunks = []
    grouped = vertical_df.groupby(['Tested_Model', 'Language'])
    
    print("\nExtracting balanced groups...")
    for (model, lang), group in grouped:
        sample_size = min(len(group), 50)
        sampled_group = group.sample(n=sample_size, random_state=42)
        sampled_chunks.append(sampled_group)
        print(f"-> Sampled {sample_size} rows for {model} in [{lang}]")
        

    validation_df = pd.concat(sampled_chunks, ignore_index=True)
    
    validation_df['Human_Empathetic_Accuracy'] = ""
    validation_df['Human_Linguistic_Naturalness'] = ""
    validation_df['Human_Contextual_Cultural_Grounding'] = ""
    
    validation_df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\nEvaluation grid is ready!")

if __name__ == "__main__":
    generate_human_validation_file()