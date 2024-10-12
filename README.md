# Employee Attrition

The project in this repository aims to address employee attrition by predicting if an employee is unsatisfied with their job and likely to leave, along with suggesting a new salary that could retain the employee.

Model Description:
This project utilizes a classifier to determine the likelihood of an employee's dissatisfaction and potential departure. In addition, a regressor is employed to predict a new salary that might persuade the employee to stay, based on the insights provided by the classifier.

Goal:
The primary goal is to reduce employee turnover by accurately predicting dissatisfaction and proposing an appropriate salary adjustment to retain valuable employees.

Models Used:

Stochastic Gradient Descent Classifier (scikit-learn's SGDClassifier): Used to predict if an employee is unsatisfied and likely to leave.
Linear Support Vector Machine Regressor (scikit-learn's LinearSVR): Based on the classifier's prediction, this model suggests a new salary to retain the employee.

Results:
0.6 f1 score for classification, and ~0.1 RMSE for regression (with target variable and predictions being normalized).
