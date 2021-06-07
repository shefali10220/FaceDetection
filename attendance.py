import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime

path = 'images'
imagess = []
names = []
myImagesList = os.listdir(path)

for cls in myImagesList:
    crrImg= cv2.imread(f'{path}/{cls}')
    imagess.append(crrImg)
    names.append(os.path.splitext(cls)[0])

def markattendance(name):
    with open('markAttendance.csv','r+') as f:
        myDatalist = f.readlines()
        nameList = []
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList: now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        f.writelines(f'\n{name},{dtString}')


def findencodings(imagess):
    encodelst= []
    for img in imagess:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encodelst.append(encoding)
    return encodelst


encodeTest = findencodings(imagess)
print("encoding complete")

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgs = cv2.resize(img,(350,350))
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(imgs)
    encodingcurrent = face_recognition.face_encodings(imgs,faces)

    for encdfaces , faceloc in zip(encodingcurrent, faces):
        matches = face_recognition.compare_faces(encodeTest, encdfaces)
        faceDist = face_recognition.face_distance(encodeTest, encdfaces)
        matchindex = np.argmin(faceDist)

        if matches[matchindex]:
            name = names[matchindex].upper()
            print(name)
            face_loc1 = face_recognition.face_locations(img)[0]
            cv2.rectangle(img,(face_loc1[3], face_loc1[0]), (face_loc1[1], face_loc1[2]), (250, 170, 190), 2)
            cv2.putText(img,name, (face_loc1[3]-6,face_loc1[0]-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendance(name)
    cv2.imshow("webcam",img)
    cv2.waitKey(1)
