# Attendance using face detectiom
This Project detects faces using your webcam and compares it with images stored on your dektop. If the images matches,Attendance is given to the matched face.




To run this code ,make sure you install the following libraries:

      1)numpy (pip install numpy)
      
      2)opencv (pip install opencv-python)
      
      3)cmake (pip install cmake)
      
      4)dlib (pip install dlib)
      
      5)Face Regognition (pip install face-recognition)
      
Make sure you install 3,4,5 in order
To install 4 and 5, the user would have to install the communiy verion of visual studio
(visual studio:https://visualstudio.microsoft.com/downloads/)
while instaliing visual studio 2019,make sure you install c++ files in it .


The practice file helps the user understand the 3 steps to face detection and recognition 
In short they are:

step 1)Importing of image and converting it into RGB(the original images is always in BGR, we concert it to RGB so that the colours are more real to the actual image)

step 2)Finding the faces in the imported image and encoding them(for finding the faces we use face_recognition.face_locations method and for encoding we use the face_recognition.face_encodings method)

step 3)Comparing the faces and finding the distance between them(lower the face distance walue ,better the match,it roughly shows how dissimilar images are )
       (in step 3 we get the encodings and we compare these to get 128 measurements )
       
In the Attendance file ,we use the web came to use the live images
we do all the 3 steps for the image received by the web cam too
In this we make sure that images are already pre-fed in our file which contains the code .
THe images and their names are stored in a list ,and so are their encodings ,the program jst compare these and regognizes you .
After you are recognized ,your name and time are sent into a csv file(csv=comma seperated values )whihch can lated be imported as an excel file.


