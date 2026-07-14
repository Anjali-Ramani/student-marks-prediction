import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    "Hours": [2, 3, 5, 6, 8, 9],
    "Attendance": [60, 65, 70, 80, 90, 95],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features
X = df[["Hours", "Attendance"]]

# Target
y = df["Pass"]

# Decision Tree Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Prediction
prediction = model.predict([[7, 85]])

print("Prediction:", prediction)