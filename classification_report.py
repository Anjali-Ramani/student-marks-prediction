import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features
X = df[["Hours"]]

# Target
y = df["Pass"]

# Create Model
model = LogisticRegression()

# Train Model
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# Classification Report
print(classification_report(y, y_pred))