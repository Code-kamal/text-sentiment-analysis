import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from hoda_dataset import load_hoda

X_train, y_train, X_test, y_test = load_hoda()
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
pred = model.predict(X_test)
model_score= model.score(X_test, y_test)

# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\ragham_8.png", cv2.IMREAD_GRAYSCALE)
# X = cv2.resize(img, dsize=(5,5))
# X = X.reshape(1,25)

# r = model.predict(X)[0]
# plt.imshow(img, cmap='gray')
# plt.title(r)
# plt.show()

img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg") #BGR
gray = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg", cv2.IMREAD_GRAYSCALE)

#convert to binary_inverse
gray[gray>127.5] = 255
gray[gray<127.5] = 0
binary = 255 - gray

# extract connected componnets

number_of_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

for label in range(1, number_of_labels):
    x,y,w,h,_ = stats[label]
    if w>5 and h>5:
        digit = binary[y:y+h,x:x+w]
        X = cv2.resize(digit, (5,5))
        X = X.reshape(1,25)
        r = model.predict(X)[0]

        cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255),2)
        cv2.putText(img,str(r),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)

plt.figure()
plt.imshow(img[...,::-1])
