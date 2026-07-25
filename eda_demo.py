import pandas as pd

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6],
    "Attendance": [60, 65, 70, 80, 90],
    "Marks": [40, 50, 60, 75, 90]
}

df = pd.DataFrame(data)

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())