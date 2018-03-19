# import numpy
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

img = cv2.imread('durham-council.PNG', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Council', img)
print(img.shape)  # print image dimensions (size in matlab)

# print pixel (picture element) value at give (row,col) in the picture
print(img[50, 100])

fig = plt.figure(figsize=img.shape)
# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)
# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False
                    )
cb = fig.colorbar(p, shrink=0.5)

cv2.waitKey(0)
cv2.destroyAllWindows()
