import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6, 7],
    "Attendance": [60, 65, 70, 80, 90, 95],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

# Model
model = DecisionTreeClassifier(random_state=42)

# Hyperparameters
parameters = {
    "max_depth": [1, 2, 3, 4]
}

# Grid Search
grid = GridSearchCV(model, parameters, cv=3)

grid.fit(X, y)

print("Best Parameter:")
print(grid.best_params_)

print("\nBest Score:")
print(grid.best_score_)