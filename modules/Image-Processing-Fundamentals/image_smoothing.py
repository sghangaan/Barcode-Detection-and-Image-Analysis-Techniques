import cv2

# Load image
image = cv2.imread('./Image-Processing-Fundamentals/Resources/image.jpg')

# Apply Averaging filter
blur_avg = cv2.blur(image, (5, 5))

# Apply Gaussian filter
blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# Display results
cv2.imshow('Original', image)
cv2.imshow('Averaging Blur', blur_avg)
cv2.imshow('Gaussian Blur', blur_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

