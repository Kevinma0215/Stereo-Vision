import cv2 as cv
import matplotlib.pyplot as plt

# Read both images and convert to grayscale
img1 = cv.imread('images/ZED/undistortRectifystereoLeftV1.5/imageL0.tif', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('images/ZED/undistortRectifystereoRightV1.5/imageR0.tif', cv.IMREAD_GRAYSCALE)

# Compare unprocessed images
fig, axes = plt.subplots(1, 2, figsize = (15, 10))
axes[0].imshow(img1, cmap="gray")
axes[1].imshow(img2, cmap="gray")
axes[0].axhline(250)
axes[1].axhline(250)
axes[0].axhline(150)
axes[1].axhline(150)
plt.suptitle("Original images")
plt.show()