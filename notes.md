AI is the broad field of making machines perform intelligent tasks.
Machine Learning is a subset of AI where systems learn from data.
Deep Learning is a subset of Machine Learning that uses neural networks.
Data Science focuses on extracting insights and building data-driven solutions.
Regression predicts numerical values.
Classification predicts categories.

# 📅 Day 1 - Introduction to Artificial Intelligence & Machine Learning

## Topics Learned

- What is Artificial Intelligence (AI)
- What is Machine Learning (ML)
- Difference between AI and ML
- Regression vs Classification
- Dataset, Feature, and Target
- Model Training using `fit()`
- Prediction using `predict()`

## Project

- Student Marks Prediction using Linear Regression

## Key Points

- AI enables machines to mimic human intelligence.
- Machine Learning allows computers to learn from data.
- Regression predicts continuous values.
- Classification predicts categories.
- Features are input variables.
- Target is the output variable.
- `fit()` trains the model.
- `predict()` makes predictions using the trained model.

---

# 📅 Day 2 - Working with Dataset using Pandas

## Topics Learned

- Introduction to Pandas
- Reading CSV files
- Creating Feature (X)
- Creating Target (y)

## Key Points

- `pd.read_csv()` loads datasets.
- Features are stored in X.
- Target is stored in y.
- Machine Learning models require structured data.

## Project Update

- Added CSV dataset.
- Used Pandas for data preprocessing.

---

# 📅 Day 3 - Data Visualization using Matplotlib

## Topics Learned

- Scatter Plot
- Best Fit Line
- Graph Labels
- Grid
- Plot Customization

## Key Points

- `plt.scatter()` plots actual data points.
- `plt.plot()` draws the Best Fit Line.
- `xlabel()` adds X-axis label.
- `ylabel()` adds Y-axis label.
- `title()` adds graph title.
- `grid(True)` displays grid lines.

## Project Update

- Visualized Student Marks dataset.
- Displayed Best Fit Line.

---

# 📅 Day 4 - Train-Test Split

## Topics Learned

- Train-Test Split
- Model Evaluation Basics
- Predictions on Test Data

## Key Points

- Dataset is divided into Training and Testing data.
- Training data teaches the model.
- Testing data evaluates model performance.
- Common split:
  - 80% Training
  - 20% Testing
- `train_test_split()` helps prevent overfitting.

## Project Update

- Implemented Train-Test Split.
- Compared predicted values with actual values.

---

# 📅 Day 5 - Model Evaluation Metrics

## Topics Learned

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Key Points

### MAE

- Average absolute difference between actual and predicted values.
- Easy to understand.

### MSE

- Squares the errors.
- Penalizes larger errors more.

### RMSE

- Square root of MSE.
- Same unit as target variable.
- Easy to interpret.

## Project Update

- Calculated MAE
- Calculated MSE
- Calculated RMSE
- Evaluated model performance

---

# 📅 Day 6 - Multiple Linear Regression

## Topics Learned

- Multiple Linear Regression
- Multiple Input Features
- Predicting using multiple variables

## Features Used

- Hours Studied
- Sleep Hours
- Attendance

## Target

- Marks

## Key Points

- Multiple Linear Regression uses more than one feature.
- More useful for real-world datasets.
- Model learns relationship between multiple features and target.
- Prediction depends on all input features.

## Project Update

- Built Multiple Linear Regression model.
- Predicted marks using multiple inputs.

---

# 📅 Day 7 - Polynomial Regression

## Topics Learned

- Polynomial Regression
- PolynomialFeatures
- Degree 2
- Degree 3
- fit_transform()

## Key Points

- Polynomial Regression is used when data has a curved relationship.
- Linear Regression works best for straight-line relationships.
- PolynomialFeatures converts features into higher-degree features.
- Degree 2 creates:
  - X
  - X²
- Degree 3 creates:
  - X
  - X²
  - X³
- `fit_transform()` creates polynomial features.
- Polynomial Regression trains Linear Regression on transformed features.
- Used `poly.transform()` for predictions.
- Polynomial Regression models nonlinear relationships better than Linear Regression.

## Project Update

- Created polynomial features.
- Trained Polynomial Regression model.
- Predicted marks.
- Visualized Polynomial Regression graph.
