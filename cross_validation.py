import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Marks": [35, 45, 55, 65, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Hours"]]
y = df["Marks"]

# Create Model
model = LinearRegression()

# Perform 5-Fold Cross Validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("R² Score for each fold:")
print(scores)

print("\nAverage R² Score:")
print(scores.mean())