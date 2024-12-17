import numpy as np
import cv2

def region_growing(image, seed_point, threshold):
    """
    Performs region growing on an image.

    Args:
    image: The input image.
    seed_point: The coordinates of the seed point.
    threshold: The similarity threshold.

    Returns:
    A binary mask representing the segmented region.
    """
    rows, cols = image.shape
    mask = np.zeros_like(image)
    queue = [seed_point]

    while queue:
        x, y = queue.pop(0)
        if mask[x, y] == 0:
            mask[x, y] = 1
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for nx, ny in neighbors:
                if 0 <= nx < rows and 0 <= ny < cols and abs(image[x, y] - image[nx, ny]) <= threshold:
                    queue.append((nx, ny))
    
    return mask

# Example usage
image = cv2.imread("./Image-Segmentation-and-Clustering/Resources/image.jpg", 0)
seed_point = (100, 100)
threshold = 10
mask = region_growing(image, seed_point, threshold)

# Display the result
cv2.imshow("Region Growing", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
