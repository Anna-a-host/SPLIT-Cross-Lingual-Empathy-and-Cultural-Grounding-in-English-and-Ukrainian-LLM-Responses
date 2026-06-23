import pandas as pd

def generate_final_metrics_csv():
    
    final_results = {
        "Evaluation_Category": [
            "Empathetic Accuracy", 
            "Linguistic Naturalness", 
            "Contextual & Cultural Grounding"
        ],
        "Sample_Size_n": [300, 300, 300],
        "Pearson_Correlation_r": [0.198, 0.149, -0.095],
        "Raw_P_Value_Scientific": ["5.59421e-04", "9.73347e-03", "1.00980e-01"],
        "P_Value_Decimal": [0.000559421, 0.00973347, 0.100980],
        "Statistical_Significance": [
            "Highly Significant (p < 0.001)", 
            "Significant (p < 0.01)", 
            "Not Significant (p > 0.05)"
        ],
        "Mean_Absolute_Error_MAE": [0.721, 0.810, 0.892],
        "Systematic_Leniency_Bias": [0.281, 0.506, -0.114],
        "Empirical_Interpretation": [
            "Weak positive alignment; slight AI over-scoring tendency.", 
            "Weak positive alignment; severe systematic AI leniency/inflation.", 
            "Completely unaligned; erratic automated evaluation / cultural blindspot."
        ]
    }

    df = pd.DataFrame(final_results)

    output_file = "SPLIT_Benchmark_Final_Metrics.csv"
    df.to_csv(output_file, index=False)
    

if __name__ == "__main__":
    generate_final_metrics_csv()