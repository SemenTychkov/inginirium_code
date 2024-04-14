import matplotlib as plt
import cv2
import numpy
from PIL import Image, ImageEnhance
from scipy import ndimage

img = cv2.imread("scale_1200.jpg")

id_kernel = np.array([[0, 0, 0]],
                     [0, 1, 0],
                     [0, 0, 0])


flt_img = cv2.filter2D(src=img, ddepth=1, kernel=id_kernel)