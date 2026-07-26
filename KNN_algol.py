# KNN algorithm and our first model with it

# first of all import libraries you want
import pandas as pd
import numpy as np
import mglearn
from sklearn.datasets import load_iris

# load iris dataset and identify it
iris_dataset = load_iris()
# print("Keys of iris_dataset:\n", iris_dataset.keys())
# print(iris_dataset['DESCR'][:193] + "\n...")
# print("Target names:", iris_dataset["target_names"])
# print("Feature names:", iris_dataset["feature_names"])
# print("Shape of data: ", iris_dataset["data"].shape)

# Classify your data to train_data and test_data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    iris_dataset["data"],
    iris_dataset["target"],
#     test_size=0.2,
    random_state=0 # for shuffling the data
)

# create dataframe from data in X_train
# Label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(x_train, columns=iris_dataset["feature_names"])
# create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                           marker='o', hist_kwds={"bins": 20}, s=60,
                           alpha=0.8, cmap= mglearn.cm3)

# Building our first KKN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
# fit your data in knn
knn.fit(x_train, y_train)
x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(x_new)
# print("Prediction:", prediction)
# print("Predicted target name: ", iris_dataset["target_names"][prediction])

# Evaluation the Model
y_pred = knn.predict(x_test)
# print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
# print("Test set score: {:.2f}".format(knn.score(x_test, y_test)))

# for this ML model i found a new algorithm this is the best point