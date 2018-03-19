# import numpy
import cv2

# import matplotlib.pyplot as plt

img = cv2.imread('durham-council.PNG')
# cv2.imshow('Council', img)
print(img.shape)  # print image dimensions (size in matlab)

# print pixel (picture element) value at give (row,col) in the picture
print(img[50, 100])

img_red = img[:, :, 0]
cv2.imshow('Council Red', img_red)

# plot of all the column values of channel 0 at row 50
# plt.plot(img[50,:,0])
# plt.ylabel('values at row')
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
