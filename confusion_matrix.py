import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

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

# Model
model = LogisticRegression()

# Train
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Accuracy
accuracy = accuracy_score(y, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:")
print(cm)