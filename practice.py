import numpy as np
import cv2
import face_recognition
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = face_recognition.load_image_file("images/SteveJobs.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgre = cv2.resize(img, (350, 350))
face_loc = face_recognition.face_locations(imgre)[0]
encoding = face_recognition.face_encodings(imgre)[0]
cv2.rectangle(imgre, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (200, 170,90), 2)

img1 = face_recognition.load_image_file("images/Ariana-Grande.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
imgre1 = cv2.resize(img1, (350, 350))
face_loc1 = face_recognition.face_locations(imgre1)[0]
encoding1 = face_recognition.face_encodings(imgre1)[0]
cv2.rectangle(imgre1, (face_loc1[3], face_loc1[0]), (face_loc1[1], face_loc1[2]), (200, 170,90), 2)

results = face_recognition.compare_faces([encoding],encoding1 )
print(results)
face_dist = face_recognition.face_distance([encoding],encoding1)
print(face_dist)
cv2.putText(imgre1,f'{results} {round(face_dist[0],2)}', (20, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv2.imshow("image", imgre)
cv2.imshow("image1", imgre1)
cv2.waitKey(0)
