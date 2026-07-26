# Linear regression project

# import libraries or packages you need
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
rng = np.random.default_rng(42)

# create the original function with noises
x = np.linspace(-3,3,100)
y = np.sin(4*x) + x + rng.uniform(size= len(x))

# in sklearn library you have to give data in two dimensional
x = x.reshape((len(x),1))

# create train and test data split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# create regressor
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# with these lines of code you can see the weights and bias
# print(regressor.coef_)
# print(regressor.intercept_)

new_x_train = np.concatenate((x_train, np.sin(4*x_train)), axis = 1)
new_x_test = np.concatenate((x_test, np.sin(4*x_test)), axis = 1)

regressor.fit(new_x_train, y_train)
print(regressor.score(new_x_test, y_test))

from sklearn.datasets import load_boston
data = load_boston()
print(data)



