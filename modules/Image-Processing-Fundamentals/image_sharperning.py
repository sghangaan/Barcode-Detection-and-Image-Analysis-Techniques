import cv2
import numpy as np

# Load image
image = cv2.imread('./Image-Processing-Fundamentals/Resources/image.jpg')

# Sharpening kernel
kernel_sharpening = np.array([[-1, -1, -1],
[-1, 9, -1],
[-1, -1, -1]])

# Apply sharpening
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

# Display results
cv2.imshow('Original', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()