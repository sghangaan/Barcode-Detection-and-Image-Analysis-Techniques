import cv2
import numpy as np

# Create a blank image for demonstration (200x200 pixels with a white background)
image = np.ones((200, 200, 3), dtype=np.uint8) * 255


# Draw a red point at the original coordinates (50, 50)
cv2.circle(image, (50, 50), 5, (0, 0, 255), -1)


# Define source and destination points for the homography transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [220, 220]])

# Calculate the Homography matrix
homography_matrix, _ = cv2.findHomography(pts1, pts2)


# Apply Homography
projective_transformed_image = cv2.warpPerspective(image, homography_matrix,
(image.shape[1], image.shape[0]))


# Display Result
cv2.imshow('Projective Transformed Image', projective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()