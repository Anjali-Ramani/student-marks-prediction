import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input Feature
X = df[["Hours"]]

# Target
y = df["Pass"]

# Create Model
model = LogisticRegression()

# Train Model
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])

print("Prediction:", prediction)

# Prediction Probability
probability = model.predict_proba([[5]])

print("Probability:", probability)