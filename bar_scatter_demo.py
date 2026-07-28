import matplotlib.pyplot as plt

# Data
students = ["Anjali", "Rahul", "Priya", "Aman"]
marks = [90, 75, 85, 70]

# Bar Chart
plt.figure(figsize=(5,4))
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
hours = [1, 2, 3, 4, 5]
scores = [20, 35, 50, 65, 80]

plt.figure(figsize=(5,4))
plt.scatter(hours, scores)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()