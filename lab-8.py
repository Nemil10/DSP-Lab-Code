import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab import files

# File paths
source_path = '/content/image1.jpg'
reference_path = '/content/image1.jpg'

# Load images in grayscale
source_image = cv2.imread(source_path, cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

# Check if images are loaded
if source_image is None:
    print("Source image not found")
else:
    print("Source image loaded successfully")

if reference_image is None:
    print("Reference image not found")
else:
    print("Reference image loaded successfully")

# Histogram of Original Image

histogram = cv2.calcHist(
    [source_image], [0], None, [256], [0, 256]
)

plt.figure(figsize=(8, 6))
plt.title('Original Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(histogram)
plt.xlim([0, 256])
plt.grid(True)
plt.show()

# Histogram Equalization

equalized_image = cv2.equalizeHist(source_image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(source_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

# Histogram of Equalized Image

equalized_histogram = cv2.calcHist(
    [equalized_image], [0], None, [256], [0, 256]
)

plt.figure(figsize=(8, 6))
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(equalized_histogram)
plt.xlim([0, 256])
plt.grid(True)
plt.show()

# Histogram Matching
source_hist = cv2.calcHist(
    [source_image], [0], None, [256], [0, 256]
)

reference_hist = cv2.calcHist(
    [reference_image], [0], None, [256], [0, 256]
)

# Normalize histograms
source_hist = source_hist / source_hist.sum()
reference_hist = reference_hist / reference_hist.sum()

# Calculate CDF
source_cdf = source_hist.cumsum()
reference_cdf = reference_hist.cumsum()

# Create mapping
mapping = np.interp(
    source_cdf,
    reference_cdf,
    range(256)
)

# Create matched image
matched_image = mapping[source_image]
matched_image = matched_image.astype(np.uint8)

# Display Histogram Matching Result

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.title('Source Image')
plt.imshow(source_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Reference Image')
plt.imshow(reference_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Matched Image')
plt.imshow(matched_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
