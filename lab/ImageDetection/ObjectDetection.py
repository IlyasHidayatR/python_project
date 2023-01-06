from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = Image.open('lab/ImageDetection/Image1.jpg')

# Image resize to 50% of original size
image = image.resize((int(image.width * 0.5), int(image.height * 0.5)))

# Convert the image to RGB
image = image.convert('RGB')

def erosion(image):
    # Set the kernel 5x5
    kernel = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

    # Convert the image to NumPy array
    image = np.array(image)

    # Convert the kernel to NumPy array
    kernel = np.array(kernel)

    # Get the image and kernel height and width
    image_height = image.shape[0]
    image_width = image.shape[1]
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    # Calculate the padding size
    padding_height = int((kernel_height - 1) // 2)
    padding_width = int((kernel_width - 1) // 2)

    # Add padding to the image
    image = np.pad(image, ((padding_height, padding_height), (padding_width, padding_width)), 'constant')

    # Create a new image with the same size as the original image
    new_image = np.zeros((image_height, image_width), dtype=np.uint8)

     # Erosion filter
    for i in range(padding_height, image_height + padding_height):
        for j in range(padding_width, image_width + padding_width):
            # Check if the pixel is 1
            if image[i, j] == 1:
                # Loop through the kernel
                for k in range(kernel_height):
                    for l in range(kernel_width):
                        # Check if the kernel value is 1
                        if kernel[k, l] == 1:
                            # Check if the pixel in the image is 1
                            if image[i - padding_height + k, j - padding_width + l] == 1:
                                # Set the pixel value to 1
                                new_image[i - padding_height, j - padding_width] = 1

    # Convert the new image to PIL image
    new_image = Image.fromarray(new_image)
    
    return new_image

def dilation(image):
    # Set the kernel
    kernel = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

    # Convert the image to NumPy array
    image = np.array(image)

    # Convert the kernel to NumPy array
    kernel = np.array(kernel)

    # Get the image and kernel height and width
    image_height = image.shape[0]
    image_width = image.shape[1]
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    # Calculate the padding size
    padding_height = int((kernel_height - 1) // 2)
    padding_width = int((kernel_width - 1) // 2)

    # Add padding to the image
    image = np.pad(image, ((padding_height, padding_height), (padding_width, padding_width)), 'constant')

    # Create a new image with the same size as the original image
    new_image = np.zeros((image_height, image_width), dtype=np.uint8)

    # Dilation filter
    for i in range(padding_height, image_height + padding_height):
        for j in range(padding_width, image_width + padding_width):
            # Check if the pixel is 1
            if image[i, j] == 1:
                # Loop through the kernel
                for k in range(kernel_height):
                    for l in range(kernel_width):
                        # Check if the kernel value is 1
                        if kernel[k, l] == 1:
                            # Set the pixel value to 1
                            new_image[i - padding_height + k, j - padding_width + l] = 1

    # Convert the new image to PIL image
    new_image = Image.fromarray(new_image)

    return new_image

def closing(image):
    # Erosion
    image = erosion(image)

    # Dilation
    image = dilation(image)

    return image

# Segmentation
def segmentation(image, upper_color, lower_color):
    # Convert the image to NumPy array
    image = np.array(image)

    # Create a new image with the same size as the original image
    new_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Segmentation filter (RGB)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Get the pixel value
            pixel = image[i, j]

            # Check if the pixel value is in the range
            if pixel[0] >= lower_color[0] and pixel[0] <= upper_color[0] and pixel[1] >= lower_color[1] and pixel[1] <= upper_color[1] and pixel[2] >= lower_color[2] and pixel[2] <= upper_color[2]:
                # Set the pixel value to 1
                new_image[i, j] = 1

    # Convert the new image to PIL image
    new_image = Image.fromarray(new_image)

    return new_image

# Find Contours
def find_contours(image):
    # Convert the image to NumPy array
    image = np.array(image)

    # Create a new image with the same size as the original image
    new_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Find contours filter with edge detection (laplacian)
    mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # Get the pixel value
            pixel = image[i, j]

            # Check if the pixel value is 1
            if pixel == 1:
                # Get the neighborhood
                neighborhood = image[i - 1:i + 2, j - 1:j + 2]

                # Get the convolution
                convolution = np.sum(neighborhood * mask)

                # Check if the convolution is 0
                if convolution == 0:
                    # Set the pixel value to 1
                    new_image[i, j] = 1

    # Convert the new image to PIL image
    new_image = Image.fromarray(new_image)

    return new_image

# Count fruit and vegetables in the image
def count_fruit_vegetable(image):
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

    # Count how many fruits and vegetables in the image
    fruits_and_vegetables_count = {}

    # Loop through the image with color segmentation method, morphological operations, and edge detection
    for color_to_detect in color_fruits_and_vegetables:
        # Define the color boundaries in RGB color space for the color to detect
        lower_color = np.array(color_fruits_and_vegetables[color_to_detect]) - 30
        upper_color = np.array(color_fruits_and_vegetables[color_to_detect]) + 30

        # Create a mask for the colors without openCV
        mask = segmentation(image, upper_color, lower_color)

        # Apply morphological operations
        mask = erosion(mask)
        # mask = dilation(mask)
        # mask = closing(mask)

        # Find the contours
        mask = find_contours(mask)

        # Convert the mask to NumPy array
        mask = np.array(mask)

        # Make a circle around the contour
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                # Get the pixel value
                pixel = mask[i, j]

                # Check if the pixel value is 1
                if pixel == 1:
                    # Check if the pixel is in the circle area
                    if (i - 100) ** 2 + (j - 100) ** 2 <= 100 ** 2:
                        # Set the pixel value to 1
                        mask[i, j] = 1

        # Convert the mask to PIL image
        mask = Image.fromarray(mask)

        # Convert the mask to NumPy array
        mask = np.array(mask)
        
        # count the number of fruits and vegetables in the image with how many circle created by the contour
        fruits_and_vegetables_count[color_to_detect] = 0
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                # Get the pixel value
                pixel = mask[i, j]

                # Check if the pixel value is 1
                if pixel == 1:
                    # Check if the pixel is in the circle area
                    if (i - 100) ** 2 + (j - 100) ** 2 <= 100 ** 2:
                        # Count the number of fruits and vegetables in the image
                        fruits_and_vegetables_count[color_to_detect] += 1

        # Show the result of the color segmentation with matplotlib
        plt.figure(figsize=(10, 10))
        plt.imshow(mask, cmap='gray')
        plt.title(color_to_detect)
        plt.show()

    return fruits_and_vegetables_count

fruit_and_vegetable_count = count_fruit_vegetable(image)

# Print the result
print(fruit_and_vegetable_count)

# Show the result count with matplotlib
plt.figure(figsize=(10, 10))
plt.bar(fruit_and_vegetable_count.keys(), fruit_and_vegetable_count.values())
plt.title('Fruits and Vegetables Count Pixel')
plt.show()
