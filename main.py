import pandas as pd
from sklearn.linear_model import LinearRegression

# Read dataset
data = pd.read_csv("student_marks.csv")

# Input feature
X = data[["Hours"]]

# Target
y = data["Marks"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[6]])

print("Predicted Marks:", prediction)