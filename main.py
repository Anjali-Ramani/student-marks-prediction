from sklearn.linear_model import LinearRegression
import numpy as np

#Dataset (Hours Studies vs Marks)

X = np.array([[1],[2],[3],[4],[5]])

y = np.array([20,35,50,65,80])

# Create the model

model = LinearRegression()

#Train the model

model.fit(X,y)

# Predict marks for a student who studied 6 hours

prediction = model.predict([[6]])

print("Predicted Marks:", prediction)