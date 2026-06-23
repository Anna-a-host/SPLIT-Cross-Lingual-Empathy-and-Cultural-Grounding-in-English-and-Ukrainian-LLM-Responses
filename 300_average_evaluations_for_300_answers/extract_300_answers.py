import pandas as pd
import numpy as np

human_file = 'human_in_the_loop_src/balanced_human_validation_subset.csv'
gpt4o_file = 'results/evaluations_by_LLMs/evaluation_gpt-4o.csv'  
claude_file = 'results/evaluations_by_LLMs/evaluation_claude.csv'
mistral_file = 'results/evaluations_by_LLMs/evaluation_mistral.csv'

output_file = '300_average_evaluations_for_300_answers/AI_300_average_jury_scores.csv'


def calculate_vertical_averages():

    human_df = pd.read_csv(human_file)
    human_df.columns = human_df.columns.str.strip()
    
    j_claude = pd.read_csv(claude_file)
    j_gpt4o = pd.read_csv(gpt4o_file)
    j_mistral = pd.read_csv(mistral_file)
    
    for df in [j_claude, j_gpt4o, j_mistral]:
        df.columns = df.columns.str.strip()
        
    target_cols = ['Prompt_ID', 'Tested_Model', 'Language', 'Empathetic_Accuracy', 'Linguistic_Naturalness', 'Contextual_Cultural_Grounding']
    
    j_claude = j_claude[target_cols]
    j_gpt4o = j_gpt4o[target_cols]
    j_mistral = j_mistral[target_cols]
    
    all_judges = pd.concat([j_claude, j_gpt4o, j_mistral], ignore_index=True)
    grouped = all_judges.groupby(['Prompt_ID', 'Tested_Model', 'Language']).mean().reset_index()
    
    grouped = grouped.round(3)
    
    grouped = grouped.rename(columns={
        'Empathetic_Accuracy': 'AI_Empathetic_Accuracy',
        'Linguistic_Naturalness': 'AI_Linguistic_Naturalness',
        'Contextual_Cultural_Grounding': 'AI_Contextual_Cultural_Grounding'
    })
    
    final_dataset = pd.merge(
        human_df[['Prompt_ID', 'Tested_Model', 'Language']], 
        grouped, 
        on=['Prompt_ID', 'Tested_Model', 'Language'], 
        how='inner'
    )
    
    final_dataset.to_csv(output_file, index=False)
    print(f"\nSUCCESS!")

if __name__ == "__main__":
    calculate_vertical_averages()