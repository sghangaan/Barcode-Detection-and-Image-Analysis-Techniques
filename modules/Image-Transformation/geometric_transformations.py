import cv2
import numpy as np
# Create a blank image for demonstration (200x200 pixels with a white background)
image = np.ones((200, 200, 3), dtype=np.uint8) * 255

# Draw a red point at the original coordinates (50, 50)
cv2.circle(image, (50, 50), 5, (0, 0, 255), -1)

# -------------------------
# 1. Translation Example
# -------------------------

# Translation Matrix: move 50 pixels right and 30 pixels down
tx, ty = 50, 30
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])


# Apply translation
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1],
image.shape[0]))

# Draw a blue point at the new translated coordinates
cv2.circle(translated_image, (50 + tx, 50 + ty), 5, (255, 0, 0), -1)


# -------------------------
# 2. Rotation Example
# -------------------------


# Rotation Matrix: Rotate 45 degrees around the center of the image
center = (image.shape[1] // 2, image.shape[0] // 2)
angle = 45
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)


# Apply rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Draw a green point at approximately the rotated coordinates (calculations done earlier)
cv2.circle(rotated_image, (center[0] - 3, center[1] + 2), 5, (0, 255, 0), -1)

# -------------------------
# 3. Scaling Example
# -------------------------

# Scaling: Resize the image to double its original size
sx, sy = 2, 2
scaled_image = cv2.resize(image, None, fx=sx, fy=sy)

# Draw a yellow point at the new scaled coordinates
cv2.circle(scaled_image, (50 * sx, 50 * sy), 10, (0, 255, 255), -1)


# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()