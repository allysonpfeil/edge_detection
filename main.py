import os
import cv2

# Get the list of files in the specified folder
folder = 'path'
files = os.listdir(folder)

# Process each file
for file in files:
    # Construct the full file path
    file_path = os.path.join(folder, file)

    # Check if the file is a PNG image
    if file.endswith('.png'):
        # Load the image
        image = cv2.imread(file_path)
        # Resize the image
        resized_image = cv2.resize(image, (640, 640))
        # Convert the image to grayscale
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur to remove noise
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        # Use the Canny edge detection algorithm to detect edges
        edges = cv2.Canny(blur, 10, 150)
        # Save the edge map to a file
        cv2.imwrite("edges_" + file, edges)
        cv2.waitKey(0)
