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

# 📅 Day 8 - Logistic Regression

## Topics Learned

- Classification
- Logistic Regression
- Sigmoid Function
- Probability
- predict()
- predict_proba()

## Key Points

- Logistic Regression is used for Classification problems.
- It predicts categories instead of continuous values.
- Output is always between 0 and 1.
- Sigmoid Function converts output into probability.
- If probability ≥ 0.5 → Class 1
- If probability < 0.5 → Class 0
- predict() returns the final class (0 or 1).
- predict_proba() returns the probability of each class.

## Project Update

- Built first Logistic Regression model.
- Predicted Pass/Fail.
- Used predict_proba() to check confidence.

# 📅 Day 9 - Confusion Matrix & Accuracy

## Topics Learned

- Accuracy
- Confusion Matrix
- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

## Key Points

- Accuracy tells how many predictions are correct.
- Accuracy = Correct Predictions / Total Predictions.
- Confusion Matrix shows detailed prediction results.
- TP = Actual Pass, Predicted Pass.
- TN = Actual Fail, Predicted Fail.
- FP = Actual Fail, Predicted Pass.
- FN = Actual Pass, Predicted Fail.

## Output

Accuracy: 100%

Confusion Matrix:
[[3 0]
 [0 3]]

Meaning:

- TN = 3
- FP = 0
- FN = 0
- TP = 3

# 📅 Day 10 - Precision, Recall & F1-Score

## Topics Learned

- Precision
- Recall
- F1-Score
- Classification Report

## Key Points

- Accuracy tells the overall percentage of correct predictions.
- Precision = Out of all predicted positive cases, how many were actually positive.
- Recall = Out of all actual positive cases, how many were correctly predicted.
- F1-Score is the balance between Precision and Recall.
- Support tells the number of actual samples in each class.
- classification_report() prints Precision, Recall, F1-Score and Support together.

## Output

Precision: 1.00
Recall: 1.00
F1-Score: 1.00
Accuracy: 100%
Support: 3 samples for each class

# 📅 Day 11 - Data Preprocessing (Handling Missing Values)

## Topics Learned

- Data Preprocessing
- Missing (Null) Values
- isnull()
- dropna()
- fillna()

## Key Points

- Missing values are also called Null Values or NaN.
- Most Machine Learning algorithms cannot handle missing values directly.
- df.isnull() checks for missing values.
- df.isnull().sum() counts missing values in each column.
- dropna() removes rows containing missing values.
- fillna() replaces missing values, commonly with the column mean.
- Data preprocessing is an important step before training a Machine Learning model.

## Output

Missing Values:
Hours = 1
Sleep = 1
Marks = 0

Mean Values:
Hours = 4.0
Sleep = 7.25

After fillna():

- Missing Hours → 4.0
- Missing Sleep → 7.25

After dropna():
Rows with missing values were removed.

# 📅 Day 12 - Feature Scaling

## Topics Learned

- Feature Scaling
- Normalization
- Standardization
- MinMaxScaler
- StandardScaler

## Key Points

- Feature Scaling makes all features have a similar scale.
- It prevents features with larger values from dominating the model.
- Normalization scales values between 0 and 1.
- Standardization makes the mean approximately 0 and allows negative values.
- MinMaxScaler is used for Normalization.
- StandardScaler is used for Standardization.
- Feature Scaling improves the performance of many Machine Learning algorithms.

## Output

Original Dataset:
Hours = 2, 4, 6, 8, 10
Income = 200000, 400000, 600000, 800000, 1000000

After Normalization:
Range = 0 to 1

After Standardization:
Mean ≈ 0
Values include both negative and positive numbers.

# 📅 Day 13 - Encoding Categorical Data

## Topics Learned

- Categorical Data
- Label Encoding
- One-Hot Encoding
- LabelEncoder
- pd.get_dummies()

## Key Points

- Machine Learning models cannot understand text directly.
- Encoding converts categorical data into numerical values.
- Label Encoding assigns a number to each category.
- One-Hot Encoding creates a separate column for each category.
- One-Hot Encoding avoids the ordering problem.
- LabelEncoder is used for Label Encoding.
- pd.get_dummies() is used for One-Hot Encoding.

## Output

Gender:
Female → 0
Male → 1

Cities:
Delhi
Jaipur
Mumbai

One-Hot Encoding created three new columns:

- City_Delhi
- City_Jaipur
- City_Mumbai

# 📅 Day 14 - Train, Validation and Test Split

## Topics Learned

- Training Set
- Validation Set
- Test Set
- Three-way Data Splitting
- train_test_split()

## Key Points

- Training Set is used to train the model.
- Validation Set is used to compare models and tune hyperparameters.
- Test Set is used only for the final evaluation.
- The Test Set should remain unseen until the model is finalized.
- We can create Train, Validation and Test sets by calling train_test_split() twice.

## Output

Total Samples = 10

Training Set = 7
Validation Set = 1
Test Set = 2

# 📅 Day 15 - Cross Validation

## Topics Learned

- Cross Validation
- K-Fold Cross Validation
- cross_val_score()
- R² Score

## Key Points

- Cross Validation evaluates the model multiple times.
- K represents the number of folds.
- Each fold becomes the Test Set exactly once.
- The final performance is the average score of all folds.
- Cross Validation provides a more reliable estimate than a single Train-Test Split.
- Very small datasets may produce unstable or negative R² scores.

## Output

- Performed 5-Fold Cross Validation.
- Obtained one R² score for each fold.
- Calculated the average R² score using scores.mean().

# 📅 Day 16 - Overfitting, Underfitting, Bias & Variance

## Topics Learned

- Underfitting
- Good Fit
- Overfitting
- Bias
- Variance

## Key Points

- Underfitting occurs when the model is too simple.
- Overfitting occurs when the model memorizes the training data.
- A Good Fit model learns the underlying pattern and generalizes well.
- High Bias leads to Underfitting.
- High Variance leads to Overfitting.
- Overfitting can be reduced using Cross Validation, Regularization, more training data, simpler models, and feature selection.

## Graph Observation

- Green Line → Good Fit (Linear Regression)
- Red Curve → Overfitting (Polynomial Regression)
- Good Fit captures the overall trend.
- Overfitting tries to fit almost every training point.

# 📅 Day 17 - Regularization (Ridge & Lasso)

## Topics Learned

- Regularization
- Ridge Regression (L2)
- Lasso Regression (L1)
- Alpha Parameter

## Key Points

- Regularization helps reduce overfitting.
- Ridge (L2) keeps all features but reduces coefficient values.
- Lasso (L1) can make some coefficients exactly zero, performing feature selection.
- A larger alpha means stronger regularization.
- Ridge helps create a more stable model.

## Output

Linear Regression Coefficient:
9.1071

Ridge Regression Coefficient:
8.7931

Observation:

- Ridge coefficient is smaller than Linear Regression.
- Regularization reduces the impact of features without removing them.

# Day 18 - Decision Tree

- Decision Tree is a supervised machine learning algorithm.
- It makes predictions by asking a series of Yes/No questions.
- The first node is called the Root Node.
- Internal Nodes contain decision rules.
- Leaf Nodes contain the final prediction.
- Decision Trees can be used for both Classification and Regression.
- Gini Index measures the impurity of a node.
- Gini = 0 means a pure node.
- Decision Trees are easy to understand and visualize.
- They can overfit if they become too deep.

# Day 19 - Random Forest

- Random Forest is an ensemble learning algorithm.
- It is made up of multiple Decision Trees.
- Each Decision Tree makes its own prediction.
- For classification, Random Forest uses majority voting.
- For regression, it uses the average prediction.
- Random Forest reduces overfitting compared to a single Decision Tree.
- It generally provides better accuracy and more reliable predictions.
- The parameter `n_estimators` specifies the number of Decision Trees.
- It works for both Classification and Regression problems.

# Day 20 - Naive Bayes

- Naive Bayes is a probability-based machine learning algorithm.
- It assumes that features are independent of each other.
- It predicts the class with the highest probability.
- Gaussian Naive Bayes is commonly used for numerical data.
- Naive Bayes is widely used in spam detection, sentiment analysis, and text classification.
- It is simple, fast, and works well on small datasets.
- It performs both training and prediction very efficiently.

# Day 21 - K-Nearest Neighbors (KNN)

- KNN stands for K-Nearest Neighbors.
- It predicts by looking at the nearest data points.
- K is the number of nearest neighbors.
- The class with the majority of neighbors becomes the prediction.
- KNN uses distance (usually Euclidean Distance) to find similar data points.
- It is simple and effective for small datasets.
- Feature scaling is important because KNN depends on distance.

# Day 22 - Support Vector Machine (SVM)

- SVM stands for Support Vector Machine.
- It is a supervised machine learning algorithm.
- It is mainly used for classification problems.
- SVM finds the best boundary called a Hyperplane.
- It tries to maximize the margin between different classes.
- The nearest data points to the boundary are called Support Vectors.
- SVM performs well on small and medium-sized datasets.

# Day 23 - Model Evaluation Metrics

- Accuracy measures overall correctness of the model.
- Precision tells how many predicted positive cases are actually positive.
- Recall tells how many actual positive cases were correctly identified.
- F1 Score is the balance between Precision and Recall.
- Accuracy is useful when classes are balanced.
- Recall is very important in medical diagnosis because missing a positive case can be dangerous.
- Precision is important when false positives are costly.

# Day 24 - Feature Engineering

- Feature Engineering improves the quality of input data.
- Feature Selection means choosing only useful features.
- Feature Creation means creating new features from existing ones.
- Feature Transformation includes scaling, normalization, and encoding.
- Removing unnecessary features reduces noise and improves model performance.
- Good features often improve accuracy more than changing the algorithm.

# Day 25 - Bias vs Variance

- Bias measures how simple the model is.
- High Bias causes Underfitting.
- Variance measures how sensitive the model is to training data.
- High Variance causes Overfitting.
- A good machine learning model should have Low Bias and Low Variance.
- Overfitting can be reduced using Regularization, Cross Validation, more training data, and simpler models.

# Day 26 - Machine Learning Pipeline

- A Machine Learning Pipeline is the complete workflow of building an ML model.
- Steps:
  1. Data Collection
  2. Data Preprocessing
  3. Feature Selection
  4. Train-Test Split
  5. Model Training
  6. Model Evaluation
  7. Prediction
- Train-Test Split helps evaluate the model on unseen data.
- Accuracy measures how many predictions are correct.
- A well-designed pipeline makes ML projects organized and reliable.

# Day 27 - Exploratory Data Analysis (EDA)

- EDA stands for Exploratory Data Analysis.
- EDA helps us understand the dataset before training a model.
- df.head() displays the first 5 rows.
- df.tail() displays the last 5 rows.
- df.info() shows dataset information, data types, and non-null values.
- df.describe() provides statistical information like mean, min, max, and standard deviation.
- df.isnull().sum() checks for missing values.
- EDA helps identify missing values, outliers, and data quality issues.

# Day 28 - Loading CSV Files

- CSV stands for Comma-Separated Values.
- Real-world datasets are commonly stored in CSV files.
- pd.read_csv() is used to load a CSV file into a Pandas DataFrame.
- df.head() displays the first 5 rows.
- df.info() provides dataset information and data types.
- df.describe() shows statistical summaries.
- df.isnull().sum() checks for missing values.
- CSV files make it easy to work with large datasets.

# Day 29 - Data Visualization with Matplotlib

- Data Visualization represents data using graphs and charts.
- Matplotlib is a Python library used for visualization.
- plt.plot() creates a line graph.
- plt.title() adds a graph title.
- plt.xlabel() labels the X-axis.
- plt.ylabel() labels the Y-axis.
- plt.grid(True) adds grid lines for better readability.
- plt.show() displays the graph.
- A graph helps identify trends and relationships in data.
