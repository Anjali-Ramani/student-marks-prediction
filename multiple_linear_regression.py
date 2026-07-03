import pandas as pd
from sklearn.linear_model import LinearRegression

# Create Dataset
data = {
    "Hours": [2, 3, 4, 5, 6],
    "Sleep": [8, 7, 6, 8, 7],
    "Attendance": [90, 92, 95, 96, 98],
    "Marks": [40, 55, 70, 85, 95]
}

# Convert Dictionary to DataFrame
df = pd.DataFrame(data)

# Input Features
X = df[["Hours", "Sleep", "Attendance"]]

# Target
y = df["Marks"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Student Marks
prediction = model.predict([[5, 8, 95]])

print("Predicted Marks:", prediction)