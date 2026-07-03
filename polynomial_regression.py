import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([10, 20, 38, 65, 90, 130])

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

print(X_poly)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_poly, y)

# Predict
prediction = model.predict(poly.transform([[7]]))

# Plot Original Data
plt.scatter(X, y, color="blue", label="Original Data")

# Plot Polynomial Curve


X_grid = np.linspace(1, 6, 100).reshape(-1, 1)
X_grid_poly = poly.transform(X_grid)

plt.plot(
    X_grid,
    model.predict(X_grid_poly),
    color="red",
    linewidth=2,
    label="Polynomial Curve"
)

# Labels
plt.title("Polynomial Regression")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show Graph
plt.show()

print("Predicted Marks:", prediction)