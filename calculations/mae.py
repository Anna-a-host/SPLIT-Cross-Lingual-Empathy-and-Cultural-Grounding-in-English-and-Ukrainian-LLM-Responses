import pandas as pd

human_file = 'human_in_the_loop_src/balanced_human_validation_subset.csv'
ai_file = '300_average_evaluations_for_300_answers/AI_300_average_jury_scores.csv'

def calculate_all_mae():
    print("\n" + "="*60)
    print("MEAN ABSOLUTE ERROR (MAE) RESULTS")
    print("="*60)

    try:
        df_human = pd.read_csv(human_file)
        df_ai = pd.read_csv(ai_file)
    except FileNotFoundError as e:
        print(f"Error: Could not find files. Details: {e}")
        return

    df_human.columns = df_human.columns.str.strip()
    df_ai.columns = df_ai.columns.str.strip()

    merged_df = pd.merge(
        df_human, 
        df_ai, 
        on=['Prompt_ID', 'Tested_Model', 'Language'], 
        suffixes=('_human', '_ai')
    )
    
    metric_pairs = [
        ('Human_Empathetic_Accuracy', 'AI_Empathetic_Accuracy', 'Empathetic Accuracy'),
        ('Human_Linguistic_Naturalness', 'AI_Linguistic_Naturalness', 'Linguistic Naturalness'),
        ('Human_Contextual_Cultural_Grounding', 'AI_Contextual_Cultural_Grounding', 'Contextual & Cultural Grounding')
    ]

    for h_col, a_col, display_name in metric_pairs:
        if h_col in merged_df.columns and a_col in merged_df.columns:
            clean_df = merged_df[[h_col, a_col]].dropna()
            total_rows = len(clean_df)
            
            mae_score = (clean_df[h_col] - clean_df[a_col]).abs().mean()
            
            bias_score = (clean_df[a_col] - clean_df[h_col]).mean()
            
            print(f"\nEvaluation Category: {display_name}")
            print(f"  -> Total Evaluated Rows:       {total_rows}")
            print(f"  -> Mean Absolute Error (MAE):  {mae_score:.3f}")
            print(f"  -> Systematic Leniency Bias:   {bias_score:+.3f}")
        else:
            print(f"\nColumn Error: Check header spelling for '{h_col}' or '{a_col}'")


if __name__ == "__main__":
    calculate_all_mae()