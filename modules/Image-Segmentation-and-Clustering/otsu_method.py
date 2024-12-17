import cv2

# Load the image
img = cv2.imread("./Image-Segmentation-and-Clustering/Resources/image.jpg", 0)

# Apply Otsu's thresholding
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the result
cv2.imshow("Otsu Thresholding", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()