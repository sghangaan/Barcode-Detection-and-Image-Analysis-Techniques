import cv2
import numpy as np
# Create a blank image for demonstration (200x200 pixels with a whitebackground)

image = np.ones((200, 200, 3), dtype=np.uint8) * 255

# Draw a red point at the original coordinates (50, 50)
cv2.circle(image, (50, 50), 5, (0, 0, 255), -1)

# Define source and destination points for the affine transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Calculate the Affine Transformation Matrix
affine_matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation
affine_transformed_image = cv2.warpAffine(image, affine_matrix,
(image.shape[1], image.shape[0]))

# Display Result
cv2.imshow('Affine Transformed Image', affine_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()