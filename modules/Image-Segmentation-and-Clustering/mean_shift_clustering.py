import cv2
import numpy as np
from sklearn.cluster import MeanShift

# Load the image and reshape it
img = cv2.imread("./Image-Segmentation-and-Clustering/Resources/image.jpg")
img_reshaped = img.reshape((-1, 3))

# Perform mean shift clustering
ms = MeanShift()
ms.fit(img_reshaped)
labels = ms.labels_
centers = ms.cluster_centers_

# Reshape the labels and create the segmented image
labels = labels.reshape(img.shape[:2])
segmented_image = np.zeros_like(img)
for i in range(len(centers)):segmented_image[labels == i] = centers[i]

# Display the segmented image
cv2.imshow("Mean Shift Clustering", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()