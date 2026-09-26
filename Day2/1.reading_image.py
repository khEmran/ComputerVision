import cv2
import os


# # importing an image and showung
# image_path= os.path.join(".","resources","lena.png")
# # print(image_path)
# image=cv2.imread(image_path)
# print(image.shape)
# cv2.imshow("Lena's Image",image)
# cv2.waitKey(0)
# # img = cv2.imread("resources/lena.png")
# # print(img)  # prints the dimensions of the image (height, width, channels)
# # cv2.imshow("Output", img)
# # cv2.waitKey(0)



# # readimg and shaowing an video
# video_path = os.path.join(".","resources","elon.mp4")
# print(video_path)
# video = cv2.VideoCapture(video_path)
# while True:
#     success, frame= video.read()
#     cv2.imshow("Video Show", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#       break



# # Reading from webcam
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error: Could not open the webcam.")
#     exit()
# cap.set(3, 640) #3  refers to width
# cap.set(4, 480) #4 refers to height
# while True:
#    success, img = cap.read()
#    cv2.imshow("Output", img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#       break