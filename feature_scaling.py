import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Dataset
data = {
    "Hours": [2, 4, 6, 8, 10],
    "Income": [200000, 400000, 600000, 800000, 1000000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# -----------------------------
# Normalization (MinMaxScaler)
# -----------------------------
minmax = MinMaxScaler()

normalized = minmax.fit_transform(df)

normalized_df = pd.DataFrame(normalized, columns=df.columns)

print("\nNormalized Dataset:")
print(normalized_df)

# -----------------------------
# Standardization (StandardScaler)
# -----------------------------
standard = StandardScaler()

standardized = standard.fit_transform(df)

standardized_df = pd.DataFrame(standardized, columns=df.columns)

print("\nStandardized Dataset:")
print(standardized_df)