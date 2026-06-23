import pandas as pd
from scipy.stats import pearsonr

human_file = 'human_in_the_loop_src/balanced_human_validation_subset.csv'
ai_file = '300_average_evaluations_for_300_answers/AI_300_average_jury_scores.csv'

def run_correlation_analysis():
    df_human = pd.read_csv(human_file)
    df_ai = pd.read_csv(ai_file)
    
    df_human.columns = df_human.columns.str.strip()
    df_ai.columns = df_ai.columns.str.strip()
    
    merged_df = pd.merge(
        df_human, 
        df_ai, 
        on=['Prompt_ID', 'Tested_Model', 'Language'], 
        suffixes=('_human', '_ai')
    )
    
    metric_pairs = [
        ('Human_Empathetic_Accuracy', 'AI_Empathetic_Accuracy'),
        ('Human_Linguistic_Naturalness', 'AI_Linguistic_Naturalness'),
        ('Human_Contextual_Cultural_Grounding', 'AI_Contextual_Cultural_Grounding')
    ]
    
    print("\n" + "="*60)
    print("             PEARSON CORRELATION COEFFICIENT RESULTS          ")
    print("="*60)
    
    for h_col, a_col in metric_pairs:
        if h_col in merged_df.columns and a_col in merged_df.columns:
            clean_pair = merged_df[[h_col, a_col]].dropna()
            
            r_coeff, p_value = pearsonr(clean_pair[h_col], clean_pair[a_col])
            
            if abs(r_coeff) >= 0.7:
                strength = "Strong"
            elif abs(r_coeff) >= 0.4:
                strength = "Moderate"
            else:
                strength = "Weak"
                
            print(f"\nEvaluation Category: {h_col.replace('Human_', '')}")
            print(f"  -> Pearson Correlation (r):  {r_coeff:.3f}")
            print(f"  -> P-Value (Significance):   {p_value:.5e}")
            print(f"  -> Relationship Strength:    {strength}")
        else:
            print(f"\nMissing column pair error: Check names for {h_col} or {a_col}")
            

if __name__ == "__main__":
    run_correlation_analysis()