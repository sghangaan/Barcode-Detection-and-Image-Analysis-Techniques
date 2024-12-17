import cv2

# Load the image
img = cv2.imread("./Image-Segmentation-and-Clustering/Resources/image.jpg", 0)

# Apply mean adaptive thresholding
thresh1 = cv2.adaptiveThreshold(img, 255,
cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

# Apply Gaussian adaptive thresholding
thresh2 = cv2.adaptiveThreshold(img, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

# Display the results
cv2.imshow("Mean Adaptive Thresholding", thresh1)
cv2.imshow("Gaussian Adaptive Thresholding", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()