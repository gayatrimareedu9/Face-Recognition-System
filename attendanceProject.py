import cv2
import os
import face_recognition

path = 'ImagesAttendance'
images = []
classNames = []

def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imgRGB = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)

    encode = face_recognition.face_encodings(imgRGB)[0]
    print(len(encode))

    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(len(images))
print(type(images[0]))

encodeListKnown = findEncodings(images)
print(len(encodeListKnown))

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
   