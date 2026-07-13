import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 45, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X, y)

# Ridge Regression
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, y)

print("Linear Regression Coefficient:")
print(linear_model.coef_)

print("\nRidge Regression Coefficient:")
print(ridge_model.coef_)