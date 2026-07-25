import pandas as pd

# Load CSV File
df = pd.read_csv("student_marks.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())