# edge_detection_xrays

This program is designed to detect the edges of a .PNG image and save the new file without disrupting the original. Edge detection can have many applications in computer science, but for this project we will simply use two images of flowers to demonstrate the CANNY edge detection algorithm.

![flowers](https://github.com/allysonpfeil/edge_detection/assets/114772538/dfaeadd8-f594-42b3-8cd2-fba36e6e97e4)
![flowers2](https://github.com/allysonpfeil/edge_detection/assets/114772538/b984dd85-f6b0-4085-8906-25280e5038da)

Importantly, these photos are very different. The first photo is focused on a small group of flowers, while the second photo has no central focus. Thus, the first image will benefit from edge detection moreso than the busy second photo. This is helpful to keep in mind, because edge detection can only work so much. Let's continue. 

The script incorporates logic that:
  1) determines if the  image is a .PNG
  2) resizes the photo to 640x640
  3) turns the image into grayscale
  4) lightly blurs some of the noise
  5) detects the edges using the CANNY algorithm
  6) saves the new photo as "edges_" + existing file name

Now, let's run the program and see what happens to our flowers.

![edges_flowers](https://github.com/allysonpfeil/edge_detection/assets/114772538/eb559b0b-cde9-4e32-87b3-a22c6012dd72)

Looks great! Adjustments to the blur could make this image even better, but this is satisfactory. How about the second photo?

![edges_flowers2](https://github.com/allysonpfeil/edge_detection/assets/114772538/4d895442-5422-48c3-a4e9-7ff1349c8617)

You can definitely tell there are flowers here based on the shape, but this image is very noisy! Preprocessing, cropping, or using an alternative image analysis technique are all great ways to combat this issue. But, for the example, it is important to demonstrate the constraints of the algorithm.
