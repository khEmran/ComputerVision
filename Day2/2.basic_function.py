import cv2
import os


image_path = os.path.join(".", "resources", "lena.png")
print(image_path)

# # Converting an image to gray scale
# image_path = os.path.join(".", "resources", "lena.png")
# print(image_path)
# image = cv2.imread(image_path)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original Image", image)
# cv2.imshow("GrayScale Image", gray_image)
# cv2.waitKey(0)


# # Converting image to blur
# image = cv2.imread(image_path)
# blur_image = cv2.GaussianBlur(image, (15,15),0)
# cv2.imshow("Original Image", image)
# cv2.imshow("Blured Image", blur_image)
# cv2.waitKey(0)

# # Converting image to canny (skeliton)
# image = cv2.imread(image_path)
# canny_image = cv2.Canny(image, 50, 150)
# cv2.imshow("Original Image", image)
# cv2.imshow("Canny Image", canny_image)
# cv2.waitKey(0)
