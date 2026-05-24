import os
from analyzer import analyze_file
from explainer import generate_explanation

project_path = input("Enter project folder path: ")

results = []

for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            results.append(analyze_file(file_path))

if not results:
    print(" No Python files found!")
else:
    report = generate_explanation(results)
    print("\n PROJECT REPORT:\n")
    print(report)