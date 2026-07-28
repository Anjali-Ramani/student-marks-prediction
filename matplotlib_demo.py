import matplotlib.pyplot as plt

# Data
hours = [1, 2, 3, 4, 5]
marks = [20, 35, 50, 65, 80]

# Create Line Plot
plt.plot(hours, marks, marker='o')

# Add Title and Labels
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Show Grid
plt.grid(True)

# Display Graph
plt.show()