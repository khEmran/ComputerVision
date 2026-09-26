import cv2
import os

image_path = os.path.join(".", "resources", "lambo.png")
print(image_path)
image = cv2.imread(image_path)
print(image.shape)
cv2.imshow("Lambo Image", image)


resized_image = cv2.resize(image, (600, 600))
print(resized_image.shape)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
