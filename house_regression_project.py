import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LinearRegression

file_url = "https://raw.githubusercontent.com/emanhamed/Houses-dataset/master/Houses%20Dataset/HousesInfo.txt"
columns = ["bedroom", "bathroom", "area", "zipcodes", "price"]
df = pd.read_csv(file_url, sep=" ", names=columns)

# you can print the dataframe and your device will show five head and tail elements and more details about your dataframe
# print(df)
# print(df.dtypes)
# print(df["zipcodes"].value_counts())
# temp_df = df[["zipcodes", "price"]]
# print(temp_df.groupby("zipcodes").mean().astype("int32"))

zip_codes, counts = np.unique(df["zipcodes"], return_counts=True)

# for zip_code, count in zip(zip_codes, counts):
#     print(zip_code,"=>", count)
# print(len(df))

for zip_code, count in zip(zip_codes, counts):
    if count<25:
        idxs = df[df["zipcodes"] == zip_code].index
        df.drop(idxs, inplace=True)

train, test = train_test_split(df, test_size=0.2, random_state=42)

m = train["price"].max()
train_y = train["price"]/m
test_y = test["price"]/m

minmax = MinMaxScaler()
numeric_columns = ["bedroom", "bathroom", "area"]
train_numeric = minmax.fit_transform(train[numeric_columns])
test_numeric = minmax.transform(test[numeric_columns])

lbl = LabelBinarizer()
train_categorical = lbl.fit_transform(train[["zipcodes"]])
test_categorical = lbl.transform(test[["zipcodes"]])

# print(lbl.classes_)
# print(test_categorical[:2])

train_x = np.hstack([train_numeric, train_categorical])
# print(train_x.shape)
test_x = np.hstack([test_numeric, test_categorical])

est = LinearRegression()
est.fit(train_x, train_y)




