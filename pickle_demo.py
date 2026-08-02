import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7],
    "Attendance": [60, 65, 70, 80, 90, 95],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")

# Load model
with open("student_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Prediction
prediction = loaded_model.predict([[6, 85]])

print("Prediction:", prediction)