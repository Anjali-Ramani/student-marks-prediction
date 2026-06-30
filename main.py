
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error

# Load Dataset
data = pd.read_csv("student_marks.csv")

# Input Feature and Target
X = data[["Hours"]]
y = data["Marks"]

# Split Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Linear Regression Model
model = LinearRegression()

# Train the Model
model.fit(X_train, y_train)

# Generate Best Fit Line
line = model.predict(X)

# Visualize Dataset
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, line, color="red", label="Best Fit Line")

# Graph Details
plt.title("Student Marks Prediction using Linear Regression")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.grid(True)
plt.legend()

# Display Graph
plt.show()

# Predict on Testing Data
predictions = model.predict(X_test)

# Compare Predictions with Actual Values
print("Predicted Values:")
print(predictions)

print("\nActual Values:")
print(y_test.values)

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error (MAE):", mae)


mse = mean_squared_error(y_test, predictions)

print("Mean Squared Error (MSE):", mse)

rmse = root_mean_squared_error(y_test, predictions)

print("Root Mean Squared Error (RMSE):", rmse)