import matplotlib.pyplot as plt
import cv2
import numpy as np

def blur_demo(image):

    dst = cv2.blur(image, (1, 15))
    plt.imshow(dst)
    plt.savefig("1.png")


def median_blur_demo(image):
    dst = cv2.medianBlur(image, 5)
    plt.imshow(dst)
    plt.savefig("2.png")
def custom_blur_demo(image):

    kernel = np.ones([5, 5], np.float32)/25
    dst = cv2.filter2D(image, -1, kernel)
    plt.imshow(dst)
    plt.savefig("3.png")

src = cv2.imread("images.jpg")
img = cv2.resize(src,None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
plt.imshow(img)

blur_demo(img)
median_blur_demo(img)
custom_blur_demo(img)


def bi_demo(image):
    dst = cv2.bilateralFilter(image, 0, 100, 5)
    plt.imshow( dst)
    plt.savefig("4.png")


def shift_demo(image):
    dst = cv2.pyrMeanShiftFiltering(image, 10, 50)
    plt.imshow(dst)
    plt.savefig("5.png")


src = cv2.imread("images.jpg")
img = cv2.resize(src,None, fx=0.8, fy=0.8,
                 interpolation=cv2.INTER_CUBIC)
bi_demo(img)
shift_demo(img)

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv
def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    plt.imshow(image)
    plt.savefig("6.png")

src = cv2.imread("images.jpg")
plt.imshow(src)

gaussian_noise(src)
dst = cv2.GaussianBlur(src, (15, 15), 0)
plt.imshow(dst)
plt.savefig("7.png")



img=cv2.imread("images.jpg", cv2.IMREAD_COLOR)
x=cv2.Sobel(img,cv2.CV_16S, 1,0)
y=cv2.Sobel(img,cv2.CV_16S, 0,1)


absx=cv2.convertScaleAbs(x)
absy=cv2.convertScaleAbs(y)
dist=cv2.addWeighted(absx,0.5, absy,0.5,0)


plt.imshow(img)
plt.savefig("8.png")
plt.imshow(absy)
plt.savefig("9.png")
plt.imshow(absx)
plt.savefig("10.png")
plt.imshow(dist)
plt.savefig("11.png")