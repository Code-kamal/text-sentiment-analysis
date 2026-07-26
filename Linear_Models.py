# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# make dataset regression and split data to train and test
X, y, true_coefficient= make_regression(n_samples=200, n_features=30, n_informative=30, noise= 100, coef= True, random_state= 42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 140, train_size=60, random_state= 42)

# make a linear regression and fit the data
linear_regression = LinearRegression().fit(X_train, y_train)
print(linear_regression.score(X_test, y_test))

