import matplotlib.pyplot as plt
import cv2 
import numpy as np 
from scipy import ndimage
img = cv2.imread("im1.png")

id_kernel = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])

flt_img = cv2.filter2D(src=img, ddepth=-1, kernel=id_kernel)

plt.imshow(flt_img)
plt.savefig("1.png")
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(3,3), sigmaX=0, sigmaY=0)
plt.imshow(gaussian_blur)
plt.savefig("2.png")

median_blur = cv2.medianBlur(src=img, ksize=9)
plt.imshow(median_blur)
plt.savefig("3.png")

result = ndimage.maximum_filter(img, size=20)
plt.imshow(result)
plt.savefig("4.png")

result = ndimage.minimum_filter(img, size=20)
plt.savefig("p.png")
plt.imshow(result)