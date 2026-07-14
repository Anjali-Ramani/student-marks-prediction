import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Dataset
data = {
    "Hours": [2, 3, 5, 6, 8, 9],
    "Attendance": [60, 65, 70, 80, 90, 95],
    "Pass": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Plot Tree
plt.figure(figsize=(8, 6))
plot_tree(
    model,
    feature_names=["Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree")
plt.show()