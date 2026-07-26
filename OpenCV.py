import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = plt.imread(r"C:\Users\pc\OneDrive\Desktop\pictures\2d08566deabe4e50a4f30428c7b0ef82.jpg") # load image as a RGB numpy array
# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\pictures\2d08566deabe4e50a4f30428c7b0ef82.jpg") # load image as a BGR numpy array
# plt.imshow(img)

# creae a grayscale image
# gray_img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\pictures\2d08566deabe4e50a4f30428c7b0ef82.jpg", cv2.IMREAD_GRAYSCALE)
# plt.imshow(img, cmap='gray')

# create binary picture
# gray_img[gray_img>127.5]=255
# gray_img[gray_img<127.5]=0
# ret, binary = cv2.threshold(gray,127.5,255,cv2.THRESH_BINARY)

# transform background black and others white
# binary_img = 255 - gray_img
# ret, binary = cv2.threshold(gray,127.5,255,cv2.THRESH_BINARY_INV)





# a mini project that color the boxes
# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\pictures\2d08566deabe4e50a4f30428c7b0ef82.jpg", cv2.IMREAD_GRAYSCALE)
# _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# num_labels, labels = cv2.connectedComponents(img)

# Map component labels to hue val, 0-179 is the hue range in OpenCV
# label_hue = np.uint8(179*labels/np.max(labels))
# blank = np.ones_like(img) * 255
# labeled_img = cv2.merge([label_hue, blank, blank])

# Converting cvt to BGR
# labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# set bg label to black
# labeled_img[label_hue==0] = 0


# plt.figure(figsize=[10,8])
# plt.subplot(121);plt.imshow(img, cmap='gray');plt.title("Original");
# plt.subplot(122);plt.imshow(labeled_img, cmap='gray');plt.title("labeled image")





# another mini project that shows 4 and 8 components
# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\pictures\2d08566deabe4e50a4f30428c7b0ef82.jpg", 0)
# _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# _, labels_with_4_connectivity = cv2.connectedComponents(img, connectivity=4)
# _, labels_with_8_connectivity = cv2.connectedComponents(img, connectivity=8)

# label_hue4 = np.uint8(179*labels_with_4_connectivity/np.max(labels_with_4_connectivity))
# label_hue8 = np.uint8(179*labels_with_8_connectivity/np.max(labels_with_8_connectivity))

# blank = np.ones_like(img) * 255
# labeled_img4 = cv2.merge([label_hue4, blank, blank])
# labeled_img8 = cv2.merge([label_hue8, blank, blank])

# Converting cvt to BGR
# labeled_img4 = cv2.cvtColor(labeled_img4, cv2.COLOR_HSV2BGR)
# labeled_img8 = cv2.cvtColor(labeled_img8, cv2.COLOR_HSV2BGR)

# set bg label to black
# labeled_img4[label_hue4==0] = 0
# labeled_img8[label_hue8==0] = 0

# plt.figure(figsize=[10,8])
# plt.subplot(131);plt.imshow(img, cmap='gray');plt.title("Original");
# plt.subplot(132);plt.imshow(labeled_img4, cmap='gray');plt.title("labeled image with 4 connectivity");
# plt.subplot(133);plt.imshow(labeled_img8, cmap='gray');plt.title("labeled image with 8 connectivity");





# another mini_project that create a bounding box
# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg")
# gray = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg", cv2.IMREAD_GRAYSCALE)

# gray[gray>127.5]=255
# gray[gray<127.5]=0
# binary_image = 255-gray

# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)

# for label in range(1,num_labels):
#    x, y, w, h, _ = stats[label]
#    if w>5 and h>5:
#        plt.figure()
#        plt.imshow(img[y:y+h,x:x+w,:])
#        plt.show()





# another mini_project that uses rectangle method in cv2
# img = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg")
# gray = cv2.imread(r"C:\Users\pc\OneDrive\Desktop\persian-digits.jpg" ,cv2.IMREAD_GRAYSCALE)

# gray[gray>127.5]=255
# gray[gray<127.5]=0
# binary_image = 255-gray

# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)

# for label in range(1,num_labels):
#    x, y, w, h, _ = stats[label]
#    if w>5 and h>5:
#        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#plt.imshow(img[:,:,::-1])