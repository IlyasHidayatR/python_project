import cv2, time
import PySimpleGUI as sg

def faceRecord():
    camera = 0
    video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
    faceDetections = cv2.CascadeClassifier('lab/FaceRecognition/haarcascade_frontalface_default.xml')
    # Imput the id with pySimpleGUI
    layout = [[sg.Text('Masukkan ID: ', size=(15, 1), font=("Helvetica", 15)), sg.InputText(key='-INPUT-', size=(15, 1), font=("Helvetica", 15))],
                [sg.Button('Record', size=(15, 1), font=("Helvetica", 15))]]
    window = sg.Window('Face Recognition Attendance System', layout, size=(400, 200), element_justification='center', finalize=True)
    window['-INPUT-'].expand(expand_x=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Record':
            id = values['-INPUT-']
            break
    window.close()
    a = 0
    while True:
        a = a + 1
        check, frame = video.read()
        tampil = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetections.detectMultiScale(tampil, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.imwrite("lab/FaceRecognition/dataset/User." + str(id) + '.' + str(a) + ".jpg", tampil[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)
        if a > 30:
            break
    video.release()
    cv2.destroyAllWindows()

# faceRecord()