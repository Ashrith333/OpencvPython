import cv2
import  numpy  as np
print("yoyo")
#image impoting----
# img = cv2.imread("Resources/download.jpg")
#
#
# cv2.imshow("Output",img)
# cv2.waitKey(10000)
# Import video-----
# cap = cv2.VideoCapture("Resources/small.mp4")
# # while True:
# #     success, img= cap.read()
# #     cv2.imshow("Video_out",img)
# #     if cv2.waitKey(1) & 0xFF==ord('q'):
# #         break
# Import webcam----
# cap = cv2.VideoCapture(0)
# cap.set(3,640)  #lenght
# cap.set(4,480)  #width
# cap.set(10,100)  #brightness
# while True:
#     success, img= cap.read()
#     cv2.imshow("Video_out",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'): #press q to stop
#         break
# editing image------------
# img = cv2.imread("Resources/download.jpg")
# kernel = np.ones((5,5),np.uint8)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny =cv2.Canny(img,150,200) #find edges in image
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# cv2.imshow("blur",imgBlur)
# cv2.imshow("gray",imgGray)
# cv2.imshow("canny",imgCanny)
# cv2.imshow("Dialation",imgDialation)
# cv2.imshow("imgEroded",imgEroded)
# cv2.waitKey(0)
# image resize / crop--------------
# img = cv2.imread("Resources/download.jpg")
# print((img.shape)) #check dimensions
# imgResizwe = cv2.resize(img,(500,600)) #widht, height
# imgCropped= img[0:100,50:200]   #height, width
# cv2.imshow("Image",img)
# cv2.imshow("Resize",imgResizwe)
# cv2.imshow("Crop",imgCropped)
# cv2.waitKey(0)

# # draw lines or text on image-----------
#
# img = np.zeros((512,512,3),np.uint8)
# # print(img)
# # img[200:300,100:300]=255,0,0 #img[:] for whole img
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# cv2.circle(img,(400,50),30,(255,200,0),5)
#
# cv2.putText(img,"ASH IS KING" , (100,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#
# cv2.imshow("image",img)
#
# cv2.waitKey(0)

#https://www.murtazahassan.com/learn-opencv-3hours/
# img = cv2.imread("Resources/cards.jpg")
#
# width, height = 250, 350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))
#
# cv2.imshow("Image", img)
#
# cv2.imshow("Output", imgOutput)
# cv2.waitKey(0)