import pandas as pd
from sklearn.model_selection import train_test_split

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Marks": [35, 45, 55, 65, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

# Step 1: 70% Train, 30% Temporary
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# Step 2: Split the remaining 30% into Validation and Test (15% each)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42
)

print("Training Set Size:", len(X_train))
print("Validation Set Size:", len(X_val))
print("Test Set Size:", len(X_test))