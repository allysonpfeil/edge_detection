import os
import cv2

folder = 'path'
files = os.listdir(folder)

for file in files:
    file_path = os.path.join(folder, file)

    if file.endswith('.png'):
        image = cv2.imread(file_path)
        resized_image = cv2.resize(image, (640, 640))
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 10, 150)
        cv2.imwrite("edges_" + file, edges)
        cv2.waitKey(0)
