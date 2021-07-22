# faceRecognition



Technology used (Libraries):
- tkinter as tk
- tkinter import Message, Text
- cv2, os
- shutil
- csv
- numpy 
- from PIL import ImageTk,Image
- pandas 
- datetime
- time
- from itertools import count
- from functools import partial

Here we were working on Face recognition based Attendance Management System by using OpenCV(Python). One can mark thier attendance by simply facing the camera. 

How it works :

1. Run only the " ".py file.
2. Enter the "username" and "password" as "admin" and "admin@123" respectively and press "Login".
3. Fill in the required details in the gui that opens up.
4. Click on "Take Images" to register yourself.
5. Click on "Train Images" to train the dataset.
6. Click on "Detect" to recognize the image and mark the attendance.

Note : -Please make sure you are not sitting in a very dark environment.
       -While training give different profiles of your face for better training
       -Wait patiently, till the camera opens up, sometimes takes a bit of time to open up the camera depending open the computers computational power
       -Wait patiently till it train the images. Huge no of images takes a bit of time to train.
   
Additional Steps:
    - "" folder contains the images who's faces were not recognized
    - "" constists the dataset of all the students whhich stores teh students Name and ID
    - "" consists of all the attandance taken so far  

thanks:
Ashish Dubey
