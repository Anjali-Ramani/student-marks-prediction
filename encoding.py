import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "City": ["Jaipur", "Delhi", "Mumbai", "Delhi", "Jaipur"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# -----------------------
# Label Encoding
# -----------------------

le = LabelEncoder()

df["Gender_Label"] = le.fit_transform(df["Gender"])

print("\nAfter Label Encoding:")
print(df)

# -----------------------
# One-Hot Encoding
# -----------------------

one_hot = pd.get_dummies(df[["City"]])

print("\nOne-Hot Encoding:")
print(one_hot)