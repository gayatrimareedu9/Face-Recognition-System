import cv2
import os

path = "ImagesAttendance"

myList = os.listdir(path)

print(myList)

images = []

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imgRGB = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
    images.append(curImg)

print(len(images))   

print(type(images[0]))

for img in images:
    cv2.imshow("Image", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()