import pandas as pd

# Step 1: Load the raw dataset
file_path = "processed.cleveland.data"  # Update with your file path
column_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
]

# Read the raw data
data = pd.read_csv(file_path, header=None, names=column_names)

# Step 2: Replace '?' with NaN for missing values
data.replace("?", pd.NA, inplace=True)

# Step 3: Save as CSV
output_file = "heart_disease_cleaned.csv"
data.to_csv(output_file, index=False)

print(f"Dataset converted and saved as {output_file}")
