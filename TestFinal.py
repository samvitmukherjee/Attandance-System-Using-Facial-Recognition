# -- coding: utf-8 --
"""
Created on 4 November 2020

@author: Rishabh Bhasin         Samvit Mukherjee

"""

import tkinter as tk
from tkinter import Message, Text
import cv2, os
import shutil
import csv
import numpy as np
from PIL import ImageTk,Image
import pandas as pd
import datetime

import time
from itertools import count

from functools import partial



#window
admin_username = "admin"
admin_password = "admin@123"


def validateLogin(username, password):
    a = username.get()
    b = password.get()
    if (a == admin_username and b == admin_password):
        accepted()

    else:
        print("INCORRECT CREDENTIALS")



    # print("username entered :", username.get())
    # print("password entered :", password.get())
    # return


# window
tkWindow = tk.Tk()
tkWindow.geometry('450x150')
tkWindow.title('Login')

# username label and text entry box
usernameLabel = tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = tk.Label(tkWindow, text="Password").grid(row=1, column=0)
password = tk.StringVar()
passwordEntry = tk.Entry(tkWindow, textvariable=password, show='•').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)


def accepted():
    print("SUCCESSFULLY LOGGED IN")



    window = tk.Toplevel()
    # helv36 = tk.Font(family='Helvaetica', size=36, weight='bold')
    window.title("Attendance System Using Facial Recognition")

    #dialog_title = 'QUIT'
    #ialog_text = 'Are you sure?'
    # answer = messagebox.askquestion(dialog_title, dialog_text)

    # window.geometry('1280x720')

    background_image=tk.PhotoImage(file=r'Background_Image_C.png',master=window)
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #window.attributes('-fullscreen', True)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # path = "profile.jpg"

    # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    # img = ImageTk.PhotoImage(Image.open(path))

    # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    # panel = tk.Label(window, image = img)


    # panel.pack(side = "left", fill = "y", expand = "no")

    # cv_img = cv2.imread("img541.jpg")
    # x, y, no_channels = cv_img.shape
    # canvas = tk.Canvas(window, width = x, height =y)
    # canvas.pack(side="left")
    # photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    # Add a PhotoImage to the Canvas
    # canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    # msg = Message(window, text='Hello, world!')

    # Font is a tuple of (font_family, size_in_points, style_modifier_string)

    im = Image.open('Check.gif')

    class ImageLabel(tk.Label):
        """a label that displays images, and plays them if they are gifs"""
        def load(self, im):

            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)
    lbl = ImageLabel(window)
    lbl.place(x=10, y=0)
    lbl.load(im)




    message = tk.Label(window, text="Attendance System Using Facial Recognition",bg='white',fg="black",
                       height=2, font=('Algerian', 41, 'bold underline'))

    message.place(x=178, y=20)

    img = ImageTk.PhotoImage(Image.open('DTU_Logo.png'),master=window)

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(window, image = img, width=170,bg='white')
    panel.place(x=10, y=20)


    lbl = tk.Label(window, text="Enter ID", width=20, height=2, fg="red", bg="yellow", font=('Calbiri', 15, ' bold '))
    lbl.place(x=400, y=200)

    txt = tk.Entry(window, width=20,  bg="yellow", fg="red", font=('Calbiri', 15, ' bold '))
    txt.place(x=700, y=215)

    lbl2 = tk.Label(window, text="Enter Name", width=20, fg="red", bg="yellow", height=2, font=('Calbiri', 15, ' bold '))
    lbl2.place(x=400, y=300)

    txt2 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('Calbiri', 15, ' bold '))
    txt2.place(x=700, y=315)

    lbl3 = tk.Label(window, text="Notification:", width=20, fg="red", bg="yellow", height=2,
                    font=('Calbiri', 15, ' bold underline '))
    lbl3.place(x=400, y=400)

    message = tk.Label(window, text="", bg="yellow", fg="red", width=40, height=2, activebackground="yellow",
                       font=('Calbiri', 15, ' bold '))
    message.place(x=700, y=400)

    lbl3 = tk.Label(window, text="Attendance Record:", width=20, fg="red", bg="yellow", height=2,
                    font=('Calbiri', 15, ' bold  underline'))
    lbl3.place(x=400, y=650)

    message2 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=35, height=2,
                        font=('Calbiri', 15, ' bold '))
    message2.place(x=700, y=650)


    def clear():
        txt.delete(0, 'end')
        res = ""
        message.configure(text=res)


    def clear2():
        txt2.delete(0, 'end')
        res = ""
        message.configure(text=res)


    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    def TakeImages():
        Id = (txt.get())
        name = (txt2.get())
        if (is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Image Capturing', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 60:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Saved for ID : " + Id + " Name : " + name
            row = [Id, name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text=res)
        else:
            if (is_number(Id)):
                res = "Enter Alphabetical Name"
                message.configure(text=res)
            if (name.isalpha()):
                res = "Enter Numeric Id"
                message.configure(text=res)


    def TrainImages():
        recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, Id = getImagesAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Image Trained"  # +",".join(str(f) for f in Id)
        message.configure(text=res)


    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # print(imagePaths)

        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids


    def TrackImages():
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                    message.configure(text="Image Tracked")

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('Detecting Face', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        message2.configure(text=res)


    clearButton = tk.Button(window, text="Clear", command=clear, fg="red", bg="yellow", width=20, height=1,
                            activebackground="Red", font=('Calbiri', 15, ' bold '))
    clearButton.place(x=950, y=200)
    clearButton2 = tk.Button(window, text="Clear", command=clear2, fg="red", bg="yellow", width=20, height=1,
                             activebackground="Red", font=('Calbiri', 15, ' bold '))
    clearButton2.place(x=950, y=300)
    takeImg = tk.Button(window, text="Take Images", command=TakeImages, fg="red", bg="green", width=20, height=1,
                        activebackground="Red", font=('Calbiri', 15, ' bold '))
    takeImg.place(x=200, y=530)
    trainImg = tk.Button(window, text="Train Images", command=TrainImages, fg="red", bg="green", width=20, height=1,
                         activebackground="Red", font=('Calbiri', 15, ' bold '))
    trainImg.place(x=500, y=530)
    trackImg = tk.Button(window, text="Detect", command=TrackImages, fg="red", bg="green", width=20, height=1,
                         activebackground="Red", font=('Calbiri', 15, ' bold '))
    trackImg.place(x=800, y=530)
    quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="red", bg="green", width=20, height=1,
                           activebackground="Red", font=('Calbiri', 15, ' bold '))
    quitWindow.place(x=1100, y=530)
    copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,
                        font=('Calbiri', 12, 'bold underline'))
    copyWrite.tag_configure("superscript", offset=10)
    copyWrite.insert("insert", "Developed By: Rishabh And Samvit")
    copyWrite.configure(state="disabled", fg="red", bg="yellow",width=31)
    copyWrite.pack(side="left")
    copyWrite.place(x=1230, y=780)

    window.mainloop()

tkWindow.mainloop()