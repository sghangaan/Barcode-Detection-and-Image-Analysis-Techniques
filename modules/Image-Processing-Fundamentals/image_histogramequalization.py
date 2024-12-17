import cv2
import numpy as np

# Load image
image = cv2.imread('./Image-Processing-Fundamentals/Resources/image.jpg')


# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display results
cv2.imshow('Original Grayscale Image', gray_image)
cv2.imshow('Histogram Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()