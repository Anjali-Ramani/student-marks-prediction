import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    "Hours": [2, 3, 4, 5, 6],
    "Attendance": [60, 65, 70, 80, 90],
    "Marks": [40, 50, 60, 75, 90]
}

df = pd.DataFrame(data)

# Correlation Matrix
print("Correlation Matrix:\n")
print(df.corr())

# Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()