import matplotlib.pyplot as plt

# Marks Dataset
marks = [20, 25, 30, 35, 40, 45, 50, 60, 70, 90]

# Histogram
plt.figure(figsize=(6,4))
plt.hist(marks, bins=5)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(4,5))
plt.boxplot(marks)
plt.title("Box Plot of Marks")
plt.grid(True)
plt.show()