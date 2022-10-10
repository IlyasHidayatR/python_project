import cv2, time
import os
from PIL import Image

camera = 0
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
faceDetections = cv2.CascadeClassifier('lab/FaceRecognition/haarcascade_frontalface_default.xml')
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.read('lab/FaceRecognition/dataset/trainer.yml')
a = 0
while True:
    a = a + 1
    width_d, height_d = 280, 280
    check, frame = video.read()
    tampil = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetections.detectMultiScale(tampil, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, conf = recognizer.predict(cv2.resize(tampil[y:y+h,x:x+w], (width_d, height_d)))
        if id == 1:
            id = "Ilyas Hidayat Rusdy"
            # print accuracy in percentage
            conf = "{0}%".format(round(100 - conf))
            print(conf)
        else:
            id = "Unknown"
        cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Recognition", frame)
    key = cv2.waitKey(1)
    # if id == 1:
    #     print("Ilyas Hidayat Rusdy")
    #     break
    if key == ord('q'):
        break
    # else:
    #     print("Face not recognized")
video.release()
cv2.destroyAllWindows()

