import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Define results directory
results_dir = "results"
output_csv = "results_summary.csv"
output_pdf = "results_summary.pdf"
output_md = "results_summary.md"

data = []

# Iterate through all result subdirectories
for folder in os.listdir(results_dir):
    folder_path = os.path.join(results_dir, folder)
    if os.path.isdir(folder_path):
        metrics_file = os.path.join(folder_path, "metrics.csv")
        if os.path.exists(metrics_file):
            with open(metrics_file, "r") as f:
                lines = f.readlines()
                headers = lines[0].strip().split(",")
                values = lines[1].strip().split(",")
                
                metrics = dict(zip(headers, values))
                metrics["LossCurve"] = os.path.join(folder_path, "loss_curve.png")
                metrics["AccuracyCurve"] = os.path.join(folder_path, "accuracy_curve.png")
                metrics["ConfusionMatrix"] = os.path.join(folder_path, "confusion_matrix.png")
                
                data.append(metrics)

# Create DataFrame
results_df = pd.DataFrame(data)

# Save to CSV
results_df.to_csv(output_csv, index=False)

# Generate Markdown Table
with open(output_md, "w") as md:
    md.write("# Results of all the Variations\n\n")
    md.write("| ActivationFunction | HiddenSize | LearningRate | BatchSize | NumberOfEpochs | TestAccuracy | ExecutionTime | LossCurve | AccuracyCurve | ConfusionMatrix |\n")
    md.write("|------------------|------------|------------|---------|--------------|------------|-------------|-----------|-------------|---------------|\n")
    for _, row in results_df.iterrows():
        md.write(f"| {row['ActivationFunction']} | {row['HiddenSize']} | {row['LearningRate']} | {row['BatchSize']} | {row['NunberOfEpochs']} | {row['Test Accuracy']} | {row['Execution Time(in sec)']} | ![Loss]({row['LossCurve']}) | ![Accuracy]({row['AccuracyCurve']}) | ![Confusion]({row['ConfusionMatrix']}) |\n")

# # Generate PDF Report
# pdf = FPDF()
# pdf.set_auto_page_break(auto=True, margin=10)

# def add_row(pdf, row):
#     pdf.set_font("Arial", size=10)
#     pdf.cell(30, 10, row['ActivationFunction'], border=1)
#     pdf.cell(30, 10, row['HiddenSize'], border=1)
#     pdf.cell(20, 10, row['LearningRate'], border=1)
#     pdf.cell(20, 10, row['BatchSize'], border=1)
#     pdf.cell(25, 10, row['NunberOfEpochs'], border=1)
#     pdf.cell(25, 10, row['Test Accuracy'], border=1)
#     pdf.cell(30, 10, row['Execution Time(in sec)'], border=1)
#     pdf.ln()
    
#     pdf.image(row['LossCurve'], x=10, w=60)
#     pdf.image(row['AccuracyCurve'], x=80, w=60)
#     pdf.image(row['ConfusionMatrix'], x=150, w=60)
#     pdf.ln(65)

# pdf.add_page()
# pdf.set_font("Arial", style='B', size=12)
# pdf.cell(0, 10, "Neural Network Performance Analysis", ln=True, align='C')
# pdf.ln(10)

# pdf.set_font("Arial", size=10)
# pdf.cell(30, 10, "Activation", border=1)
# pdf.cell(30, 10, "Hidden Size", border=1)
# pdf.cell(20, 10, "LR", border=1)
# pdf.cell(20, 10, "Batch", border=1)
# pdf.cell(25, 10, "Epochs", border=1)
# pdf.cell(25, 10, "Accuracy", border=1)
# pdf.cell(30, 10, "Exec Time", border=1)
# pdf.ln()

# for _, row in results_df.iterrows():
#     add_row(pdf, row)

# pdf.output(output_pdf)

# print(f"Results summary saved to {output_csv}, {output_md}, and {output_pdf}")
