import pandas as pd

# Create Dataset
data = {
    "Hours": [2, 3, None, 5, 6],
    "Sleep": [8, None, 7, 6, 8],
    "Marks": [35, 50, 65, 80, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values using Mean
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nDataset after Filling Missing Values:")
print(df_filled)

# Remove Missing Values
df_dropped = df.dropna()

print("\nDataset after Removing Missing Values:")
print(df_dropped)