"""
Created on 4 November 2020

@author: Rishabh Bhasin
         Samvit Mukherjee

"""
## LIBRARIES USED

# Library for TKINTER GUI
import tkinter as tk

# Library to perform CRUD operations in csv/excel
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time

# Other Dependencies
import cv2, os
from itertools import count
from functools import partial



#Login Id-Password
admin_username = "admin"
admin_password = "admin@123"


# Login Window
tkWindow = tk.Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login')

# username label and text entry box
usernameLabel = tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = tk.Label(tkWindow, text="Password").grid(row=1, column=0)
password = tk.StringVar()
passwordEntry = tk.Entry(tkWindow, textvariable=password, show='•').grid(row=1, column=1)

# Credentials

def validateLogin(username, password):
    a = username.get()
    b = password.get()
    if (a == admin_username and b == admin_password):
        accepted()

    else:
        print("INCORRECT CREDENTIALS")
        Invalid = tk.Tk()
        Invalid.geometry('150x50')
        Invalid.title('Invalid Details!')
        label = tk.Label(Invalid, text="Wrong Password!", fg="black").grid(row=6, column=1)
        Invalid.mainloop()


validateLogin = partial(validateLogin, username, password)

# login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=1)

# ----------------------------------Main Code Starts Here-----------------------------------------------------------
def accepted():
    print("SUCCESSFULLY LOGGED IN")

    #-------------------------------------Main GUI Interface---------------------------------------------

    window = tk.Toplevel()
    window.geometry('1920x1080')
    window.title("Attendance System Using Facial Recognition")

    #--------------------------------------------------Applying Background Image--------------------------------------
    background_image=tk.PhotoImage(file=r'Background_Image_C.png')
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #window.grid_rowconfigure(0, weight=1)
    #window.grid_columnconfigure(0, weight=1)

    #------------------------------------------------------Applying GIF-----------------------------------------------
    im = Image.open('Check.gif')

    class ImageLabel(tk.Label):

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

    #------------------------------------Labels And Entries-------------------------------------------------


    message = tk.Label(window, text="Attendance System Using Facial Recognition",bg='white',fg="black",
                       height=2, font=('Algerian', 41, 'bold underline'))

    message.place(x=178, y=20)

    img = ImageTk.PhotoImage(Image.open('DTU_Logo.png'))

    panel = tk.Label(window, image = img, width=170,bg='white')
    panel.place(x=10, y=20)


    lbl = tk.Label(window, text="Enter ID", width=20, height=2, fg="red", bg="yellow", font=('Calbiri', 15, ' bold'))
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

    copyWrite = tk.Label(window, fg='red', bg='yellow', text="Developed By:Rishabh And Samvit",
                         font=('Calbiri', 12, 'bold underline'))
    copyWrite.place(x=1235, y=765)

    # ------------------------------------------Functions-------------------------------------------------------
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
        res = "Image Trained"
        message.configure(text=res)


    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # print(imagePaths)

        # create empty face list
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

    # -------------------------------------------Buttons----------------------------------------------------------------
    clearButton = tk.Button(window, text="Clear", command=clear, fg="red",bg='yellow', width=20, height=1,
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

    window.mainloop()

tkWindow.mainloop()