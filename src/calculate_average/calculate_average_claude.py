import csv
import os
from collections import defaultdict

INPUT_GPT_CSV = "results/evaluations_by_LLMs/evaluation_claude.csv" 
OUTPUT_SUMMARY_CSV = "results/summary_averages/average_claude.csv"

def calculate_and_save_metrics(input_path, output_path):

    if not os.path.exists(input_path):
        print(f"Error: Could not find evaluation file at '{input_path}'")
        return

    stats = defaultdict(lambda: [[], [], []])

    with open(input_path, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            model = row["Tested_Model"]
            lang = row["Language"]
            key = (model, lang)
            
            try:
                emp = float(row["Empathetic_Accuracy"])
                ling = float(row["Linguistic_Naturalness"])
                cult = float(row["Contextual_Cultural_Grounding"])
                
                stats[key][0].append(emp)
                stats[key][1].append(ling)
                stats[key][2].append(cult)

            except (ValueError, KeyError):
                continue

    fieldnames = [
        "Tested_Model", "Language", 
        "Empathetic_Accuracy_Mean", "Linguistic_Naturalness_Mean", "Contextual_Cultural_Grounding_Mean"
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for (model, lang) in sorted(stats.keys(), key=lambda x: (x[1], x[0])):
            emp_avg = sum(stats[(model, lang)][0]) / len(stats[(model, lang)][0])
            ling_avg = sum(stats[(model, lang)][1]) / len(stats[(model, lang)][1])
            cult_avg = sum(stats[(model, lang)][2]) / len(stats[(model, lang)][2])
            
            emp_formatted = round(emp_avg, 3)
            ling_formatted = round(ling_avg, 3)
            cult_formatted = round(cult_avg, 3)

            writer.writerow({
                "Tested_Model": model,
                "Language": lang,
                "Empathetic_Accuracy_Mean": f"{emp_formatted:.3f}",
                "Linguistic_Naturalness_Mean": f"{ling_formatted:.3f}",
                "Contextual_Cultural_Grounding_Mean": f"{cult_formatted:.3f}"
            })

            print(f"{model:<14} | {lang:<5} | {emp_avg:<17.3f} | {ling_avg:<17.3f} | {cult_avg:<17.3f}")
        
    
    print(f"Summary table successfully compiled and locked down inside: {output_path}")



if __name__ == "__main__":
    calculate_and_save_metrics(INPUT_GPT_CSV, OUTPUT_SUMMARY_CSV)