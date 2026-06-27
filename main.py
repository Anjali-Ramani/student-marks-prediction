import pandas as pd
import matplotlib.pyplot as plt
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

# Best Fit Line
line = model.predict(X)

# Scatter Plot
plt.scatter(X, y, color="blue")

# Best Fit Line
plt.plot(X, line, color="red")

# Graph Title
plt.title("Hours Studied vs Marks")

# X-axis Label
plt.xlabel("Hours Studied")

# Y-axis Label
plt.ylabel("Marks")

# Grid
plt.grid(True)

# Show Graph
plt.show()

# Predict for 6 hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction)