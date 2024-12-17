import cv2
import numpy as np
from sklearn.cluster import KMeans

# Load the image and reshape it
img = cv2.imread("./Image-Segmentation-and-Clustering/Resources/image.jpg")
img_reshaped = img.reshape((-1, 3))

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(img_reshaped)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Reshape the labels and create the segmented image
labels = labels.reshape(img.shape[:2])
segmented_image = np.zeros_like(img)
for i in range(len(centers)): segmented_image[labels == i] = centers[i]

# Display the segmented image
cv2.imshow("K-Means Clustering", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()