import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab/ImageDetection/Image1.jpg')

# Image resize to 50% of original size
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Convert image to numpy array
image = np.array(image)

# Convert the image to RGB color space
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Color fruits and vegetables in RGB color space
color_fruits_and_vegetables = {
    # Fruits
    'Apple': (255, 0, 0),
    'Banana': (255, 255, 0),
    'Orange': (255, 165, 0),
    'Strawberry': (255, 0, 255),
    'Watermelon': (255, 255, 255),
    # Vegetables
    'Carrot': (255, 165, 0),
    'Cucumber': (0, 255, 0),
    'Lettuce': (0, 255, 0),
    'Onion': (255, 0, 0),
    'Tomato': (255, 0, 0)
}

# Define the color boundaries in RGB color space for the color to detect
color_to_detect = 'Tomato'
lower_color = np.array(color_fruits_and_vegetables[color_to_detect]) - 40
upper_color = np.array(color_fruits_and_vegetables[color_to_detect]) + 40

# Create a mask for the colors
mask = cv2.inRange(rgb_image, lower_color, upper_color)

# Mask the image to only select the colors
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Apply a threshold to the image
_, segmented_image = cv2.threshold(segmented_image, 10, 255, cv2.THRESH_BINARY)

# Apply a morphological operation to the image with a 5x5 kernel and Close operation
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(segmented_image, cv2.MORPH_CLOSE, kernel)

# Convert the image to grayscale
gray_image = cv2.cvtColor(closing, cv2.COLOR_BGR2GRAY)

# Find the contours of the image
contours, _ = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop the result apple location in image with rectangle
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, color_to_detect, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Count the number of apples with how many rectangle
if len(contours) == 0:
    print("No Fruit detected")
else:
    print("The total number" + " " + color_to_detect + " " + "detected:" + " " + str(len(contours)))

# Show the result
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("The total number" + " " + color_to_detect + " " + "detected:" + " " + str(len(contours)))
plt.subplot(2, 2, 2)
plt.imshow(mask)
plt.title("Mask")
plt.subplot(2, 2, 3)
plt.imshow(segmented_image)
plt.title("Segmented Image")
plt.subplot(2, 2, 4)
plt.imshow(closing)
plt.title("Closing")
plt.show()
# cv2.imshow("Original Image", image)
# cv2.imshow("Mask", mask)
# cv2.imshow("Segmented Image", segmented_image)
# cv2.imshow("Closing", closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
