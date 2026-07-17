import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7],
    "Attendance": [60, 65, 70, 80, 90, 95],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features
X = df[["Hours", "Attendance"]]

# Target
y = df["Pass"]

# KNN Model
model = KNeighborsClassifier(n_neighbors=3)

# Train
model.fit(X, y)

# Prediction
prediction = model.predict([[6, 85]])

print("Prediction:", prediction)