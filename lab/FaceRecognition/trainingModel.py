# make model for face recognition with OpenCV method eigenfaces
# https://docs.opencv.org/3.4.1/da/d60/tutorial_face_main.html
# https://docs.opencv.org/3.4.1/d9/d70/classcv_1_1FaceRecognizer.html
# https://docs.opencv.org/3.4.1/d1/d4a/classcv_1_1face_1_1EigenFaceRecognizer.html
# https://docs.opencv.org/3.4.1/d1/d4a/classcv_1_1face_1_1EigenFaceRecognizer.html#a0f3b4f3e5e3d6c7b9d8c3b8e8f3b3c3e

import cv2, os, numpy as np
from PIL import Image

# Path for face image database
# path = 'lab/FaceRecognition/dataset'

recognizer = cv2.face.EigenFaceRecognizer_create()
detector = cv2.CascadeClassifier("lab/FaceRecognition/haarcascade_frontalface_default.xml");

# function to get the images and label data
def getImagesAndLabels(path):
    width_d, height_d = 280, 280
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] # get the path of all the images in the folder (dataset)
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8') # convert PIL image to numpy array
        id = int(os.path.split(imagePath)[-1].split(".")[1]) # get the image id
        faces = detector.detectMultiScale(img_numpy) # get the face from the training images
        for (x,y,w,h) in faces:
            faceSamples.append(cv2.resize(img_numpy[y:y+h,x:x+w], (width_d, height_d))) # add the image to face samples list
            ids.append(id) # add the id to ids list
    return faceSamples,ids # return the face samples list and ids list

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels('lab/FaceRecognition/dataset') # get the faces and ids list
recognizer.train(faces, np.array(ids)) # train the model using the faces and ids list

# Save the model into trainer/trainer.yml
recognizer.write('lab/FaceRecognition/dataset/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids)))) # print the numer of faces trained and end program