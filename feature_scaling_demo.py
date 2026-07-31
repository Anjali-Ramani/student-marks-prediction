import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Dataset
data = {
    "Hours": [2, 4, 6, 8, 10],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# Standard Scaling
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)

print("\nStandardScaler Output:\n")
print(standard_scaled)

# Min-Max Scaling
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)

print("\nMinMaxScaler Output:\n")
print(minmax_scaled)