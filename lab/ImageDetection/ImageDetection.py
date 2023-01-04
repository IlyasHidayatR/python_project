from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = Image.open('lab/ImageDetection/Image2.jpg')

# Image resize to 50% of original size
image = image.resize((int(image.width * 0.5), int(image.height * 0.5)))

# Detect fruits and vegetables in the image with color space and color segmentation and count them
def detect_fruits_and_vegetables(image):
    # Convert the image to RGB color space
    image = image.convert('RGB')

    # Define colors to detect for each fruit and vegetable in RGB color space
    color_fruits_and_vegetables = {
        # Fruits
        'Apple': (255, 0, 0),
        'Blueberry': (0, 0, 255),
        'Orange': (255, 165, 0),
        'Strawberry': (255, 0, 0),
        'Green Apple': (0, 255, 0),
        'Grapes': (255, 0, 0),
        # Vegetables
        'Carrot': (255, 165, 0),
        'Cucumber': (0, 255, 0),
        'Lettuce': (0, 255, 0),
        'Onion': (255, 0, 0),
        'Tomato': (255, 0, 0)
    }

    # Convert the image to NumPy array
    image = np.array(image)

    # Count the fruits and vegetables with morfology operation and show the result location in image with rectangle
    fruits_and_vegetables_count = {}
    for color_to_detect in color_fruits_and_vegetables:
        # Define the color boundaries in RGB color space for the color to detect
        lower_color = np.array(color_fruits_and_vegetables[color_to_detect]) - 30
        upper_color = np.array(color_fruits_and_vegetables[color_to_detect]) + 30

        # Create a mask for the colors
        mask = cv2.inRange(image, lower_color, upper_color)

        # Mask the image to only select the colors to detect
        segmented_image = cv2.bitwise_and(image, image, mask=mask)

        # Apply a threshold to the image
        _, segmented_image = cv2.threshold(segmented_image, 10, 255, cv2.THRESH_BINARY)

        # Apply a morphological operation to the image with a 5x5 kernel and Close operation
        kernel = np.ones((5, 5), np.uint8)
        segmented_image = cv2.morphologyEx(segmented_image, cv2.MORPH_CLOSE, kernel)

        # Convert the image to grayscale color space
        segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)

        # Find the contours of the image with OpenCV
        contours, _ = cv2.findContours(segmented_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Count the fruits and vegetables
        fruits_and_vegetables_count[color_to_detect] = len(contours)

        # Draw the rectangle around the fruits and vegetables
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, color_to_detect, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with the rectangle around the fruits and vegetables 
    plt.title('Fruits and Vegetables Detection')
    plt.imshow(image)
    plt.show()

    return fruits_and_vegetables_count
    
# Detect fruits and vegetables in the image
fruits_and_vegetables_count = detect_fruits_and_vegetables(image)

# Print the fruits and vegetables count
print(fruits_and_vegetables_count)

# Show the results for the fruits and vegetables count in a bar chart
plt.bar(fruits_and_vegetables_count.keys(), fruits_and_vegetables_count.values())
plt.xticks(rotation=90)
plt.show()
