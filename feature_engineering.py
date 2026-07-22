import pandas as pd

# Original Dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya"],
    "Hours": [2, 5, 6, 7],
    "Attendance": [60, 80, 90, 95],
    "Favorite_Color": ["Red", "Blue", "Green", "Black"],
    "Pass": [0, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Feature Selection
X = df[["Hours", "Attendance"]]

print("\nSelected Features:\n")
print(X)