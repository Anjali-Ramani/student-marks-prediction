import pandas as pd
from sklearn.svm import SVC

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

# SVM Model
model = SVC(kernel="linear")

# Train
model.fit(X, y)

# Prediction
prediction = model.predict([[6, 85]])

print("Prediction:", prediction)