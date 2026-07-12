import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Linear Regression (Good Fit)
linear_model = LinearRegression()
linear_model.fit(X, y)

# Polynomial Regression (Degree 4)
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Predictions
X_range = np.linspace(1, 5, 100).reshape(-1, 1)

plt.scatter(X, y, color="blue", label="Data")

# Linear Line
plt.plot(
    X_range,
    linear_model.predict(X_range),
    color="green",
    label="Good Fit"
)

# Polynomial Curve
plt.plot(
    X_range,
    poly_model.predict(poly.transform(X_range)),
    color="red",
    label="Overfitting"
)

plt.title("Good Fit vs Overfitting")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.show()