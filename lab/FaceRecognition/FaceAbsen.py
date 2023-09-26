import cv2
import os
from PIL import Image
import numpy as np
import csv
import pandas as pd
import datetime
import PySimpleGUI as sg
import recordFace
import trainingModel

# Path to the dataset
path = 'lab/FaceRecognition/dataset'

# Path to the trained model
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.read('lab/FaceRecognition/dataset/trainer.yml')

# Path to the haarcascade
faceDetections = cv2.CascadeClassifier('lab/FaceRecognition/haarcascade_frontalface_default.xml')

# Path to the attendance file
attendance = 'lab/FaceRecognition/attendance.csv'

# Main function
def main():
    # Get the current date
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    # Get the current time
    time = now.strftime("%H:%M:%S")

    # Initialize the camera and size
    camera = 0
    video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

    # Initialize the window 
    sg.theme('DarkAmber')
    layout = [[sg.Text('Face Recognition Attendance System', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                [sg.Text('Name: ', size=(8, 1), font=("Helvetica", 15)), sg.Text('', size=(15, 1), font=("Helvetica", 15), key='-OUTPUT-')],
                [sg.Text('Date: ', size=(8, 1), font=("Helvetica", 15)), sg.Text(date, size=(15, 1), font=("Helvetica", 15), key='-OUTPUT3-')],
                [sg.Text('Time: ', size=(8, 1), font=("Helvetica", 15)), sg.Text(time, size=(15, 1), font=("Helvetica", 15), key='-OUTPUT2-')],
                [sg.Button('Record Face', size=(15, 1), font=("Helvetica", 15)), sg.Button('Train Face', size=(15, 1), font=("Helvetica", 15))],
                [sg.Image(filename='', key='-IMAGE-', size=(280, 280))],
                [sg.Button('Start', size=(10, 1), font=("Helvetica", 15)), sg.Button('Stop', size=(10, 1), font=("Helvetica", 15)), sg.Button('Exit', size=(10, 1), font=("Helvetica", 15)), sg.Button('Show Attendance', size=(15, 1), font=("Helvetica", 15)), sg.Button('Clear Attendance', size=(15, 1), font=("Helvetica", 15))]]
    window = sg.Window('Face Recognition Attendance System', layout, size=(800, 900), element_justification='center', finalize=True)
    window['-OUTPUT-'].expand(expand_x=True)
    window['-OUTPUT2-'].expand(expand_x=True)
    window['-OUTPUT3-'].expand(expand_x=True)

    # Initialize the variables
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # Initialize the list
    names = []
    dates = []
    times = []

    # Initialize the dataframe
    df = pd.DataFrame()

    # Initialize the csv file
    with open(attendance, 'a+', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Name', 'Date', 'Time'])

    # Main loop
    while True:
        # Read the frame from the camera
        check, frame = video.read()

        # Convert to grayscale
        tampil = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceDetections.detectMultiScale(tampil, scaleFactor=1.3, minNeighbors=5)

        # Draw a rectangle around the face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Recognize the face (calculate the distance between the face and the faces in the dataset)
            id, conf = recognizer.predict(cv2.resize(tampil[y:y+h,x:x+w], (280, 280)))

            # If the distance is less than 500, then the face is recognized
            if conf > 500:
                if id == 1:
                    id = "Ilyas Hidayat Rusdy"
                    # print confidence dalam persen
                    window['-OUTPUT-'].update(id)
                    conf = "{0}%".format(round(conf-100))
                    print(conf)
                    a = a + 1
                    if a == 1:
                        # Make date move everyday
                        day = datetime.datetime.now()
                        date = day.strftime("%Y-%m-%d")
                        # Make time move every second
                        now = datetime.datetime.now()
                        time = now.strftime("%H:%M:%S")
                        names.append(id)
                        dates.append(date)
                        times.append(time)
                        df['Name'] = names
                        df['Date'] = dates
                        df['Time'] = times
                        with open(attendance, 'a+', newline='') as csvFile:
                            csvWriter = csv.writer(csvFile)
                            csvWriter.writerow([id, date, time])
                            
                else:
                    id = "Unknown"
            else:
                id = "Unknown"
            cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the resulting frame
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        window['-IMAGE-'].update(data=imgbytes)

        # Read the events
        event, values = window.read(timeout=20)

        # Time and date
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        window['-OUTPUT2-'].update(time)
        window['-OUTPUT3-'].update(date)

        # If the 'Exit' button is clicked, then exit the program
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # If the 'Start' button is clicked, then start the program
        if event == 'Start':
            # If the 'Start' button is clicked for the first time, then start the program
            if b == 0:
                a = 0
                b = 1
                c = 0
                d = 0
                e = 0
                names = []
                dates = []
                times = []
                df = pd.DataFrame()
                with open(attendance, 'a+', newline='') as csvFile:
                    csvWriter = csv.writer(csvFile)
                    csvWriter.writerow(['Name', 'Date', 'Time'])

            # If the 'Start' button is clicked for the second time, then continue the program
            if b == 1:
                b = 0
                c = 0
                d = 0
                e = 1

        # If the 'Stop' button is clicked, then stop the program
        if event == 'Stop':
            # If the 'Stop' button is clicked for the first time, then stop the program
            if c == 0:
                a = 0
                b = 0
                c = 1
                d = 0
                e = 0
                names = []
                dates = []
                times = []
                df = pd.DataFrame()
                with open(attendance, 'a+', newline='') as csvFile:
                    csvWriter = csv.writer(csvFile)
                    csvWriter.writerow(['Name', 'Date', 'Time'])

        # If the 'Show Attendance' button is clicked, then show the attendance
        if event == 'Show Attendance':
            # If the 'Show Attendance' button is clicked for the first time, then show the attendance
            if d == 0:
                a = 0
                b = 0
                c = 0
                d = 1
                e = 0
                sg.popup_scrolled(df.to_string(), title='Attendance', size=(800, 700))

        # If the 'Clear Attendance' button is clicked, then clear the attendance
        if event == 'Clear Attendance':
            # If the 'Clear Attendance' button is clicked for the first time, then clear the attendance
            if e == 0:
                a = 0
                b = 0
                c = 0
                d = 0
                e = 1
                names = []
                dates = []
                times = []
                df = pd.DataFrame()
                with open(attendance, 'w', newline='') as csvFile:
                    csvWriter = csv.writer(csvFile)
                    csvWriter.writerow(['Name', 'Date', 'Time'])

        # If the 'Record Face' button is clicked, then record the face
        if event == 'Record Face':
            recordFace.faceRecord()

        # If the 'Train Face' button is clicked, then train the face
        if event == 'Train Face':
            trainingModel.trainModel()

    # Release the camera
    video.release()

    # Close the window
    window.close()

#  Main function
if __name__ == "__main__":
    main()