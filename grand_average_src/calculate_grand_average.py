import csv
import os
from collections import defaultdict

SUMMARY_DIR = "results/summary_averages"
OUTPUT_FILE = "grand_average_src/grand_average.csv"

def calculate_final_ensemble_means():
    if not os.path.exists(SUMMARY_DIR):
        print(f"Error: Could not find directory '{SUMMARY_DIR}'")
        return

    combined_data = defaultdict(lambda: {"emp": [], "ling": [], "cult": []})
    
    csv_files = [f for f in os.listdir(SUMMARY_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"Warning: No CSV files found inside '{SUMMARY_DIR}'")
        return
    
    print(f"Found {len(csv_files)} judge summary files to combine: {csv_files}")


    for filename in csv_files:
        file_path = os.path.join(SUMMARY_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    model = row["Tested_Model"]
                    lang = row["Language"]
                    key = (model, lang)
                    
                    combined_data[key]["emp"].append(float(row["Empathetic_Accuracy_Mean"]))
                    combined_data[key]["ling"].append(float(row["Linguistic_Naturalness_Mean"]))
                    combined_data[key]["cult"].append(float(row["Contextual_Cultural_Grounding_Mean"]))

                except (ValueError, KeyError) as e:
                    continue


    fieldnames = [
        "Tested_Model", "Language", 
        "Final_Empathetic_Accuracy_Mean", "Final_Linguistic_Naturalness_Mean", "Final_Contextual_Cultural_Grounding_Mean"
    ]


    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        print("\n" + "="*90)
        print(" FINAL CONSOLIDATED ENSEMBLE MEANS (GRAND AVERAGE ACROSS ALL THREE JUDGES) ")
        print("="*90)
        print(f"{'Tested Model':<14} | {'Lang':<5} | {'Grand Emp. Mean':<17} | {'Grand Ling. Mean':<17} | {'Grand Cult. Mean':<17}")
        print("-"*90)


        for (model, lang) in sorted(combined_data.keys(), key=lambda x: (x[1], x[0])):
            emp_list = combined_data[(model, lang)]["emp"]
            ling_list = combined_data[(model, lang)]["ling"]
            cult_list = combined_data[(model, lang)]["cult"]
            
            grand_emp = sum(emp_list) / len(emp_list)
            grand_ling = sum(ling_list) / len(ling_list)
            grand_cult = sum(cult_list) / len(cult_list)

            writer.writerow({
                "Tested_Model": model,
                "Language": lang,
                "Final_Empathetic_Accuracy_Mean": f"{grand_emp:.3f}",
                "Final_Linguistic_Naturalness_Mean": f"{grand_ling:.3f}",
                "Final_Contextual_Cultural_Grounding_Mean": f"{grand_cult:.3f}"
            })

            print(f"{model:<14} | {lang:<5} | {grand_emp:<17.3f} | {grand_ling:<17.3f} | {grand_cult:<17.3f}")
    
    print(f"✓ Master final averages compiled and locked down here: {OUTPUT_FILE}")

if __name__ == "__main__":
    calculate_final_ensemble_means()