import os
import pandas as pd

input_file = 'human_in_the_loop_src/balanced_human_validation_subset.csv'  
output_file = 'human_in_the_loop_src/human_averages_summary.csv'

def calculate_human_averages():
    if not os.path.exists(input_file):
        print(f"Error: Could not find '{input_file}' in the current directory.")
        
    df = pd.read_csv(input_file)
    
    df.columns = df.columns.str.strip()
    
    score_columns = [
        'Human_Empathetic_Accuracy',
        'Human_Linguistic_Naturalness',
        'Human_Contextual_Cultural_Grounding' 
    ]
    
    summary_df = df.groupby(['Language', 'Tested_Model'])[score_columns].mean().reset_index()
    summary_df = summary_df.round(3)
    
    summary_df.columns = [
        'Language',
        'Tested_Model',  
        'Human_Empathetic_Accuracy_Mean', 
        'Human_Linguistic_Naturalness_Mean', 
        'Human_Contextual_Cultural_Grounding_Mean'
    ]
    
    summary_df.to_csv(output_file, index=False)
    
    print(f"SUCCESS: Averages calculated and saved to '{output_file}'!")

if __name__ == "__main__":
    calculate_human_averages()