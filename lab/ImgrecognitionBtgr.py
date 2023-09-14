# In[]:
# import data from the dataset folder dataset_images
import os
import cv2
import numpy as np

# read the dataset images jpg
dataset = []
for i in os.listdir('lab/dataset_image'):
    img = cv2.imread('lab/dataset_image/'+i)
    dataset.append(img)
# show the dataset images
dataset

# label the dataset images with name batagor
batagor = []
for i in dataset:
    batagor.append('batagor')
# show the label
batagor

# make dataset images to array
dataset = np.array(dataset)
# show the shape of the dataset
dataset.shape

# make label to array
batagor = np.array(batagor)
# show the shape of the label
batagor.shape

#  Make model with keras Sequential
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

# make data training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(dataset,batagor,test_size=0.2,random_state=0)

# compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# train the model
model.fit(X_train,y_train,epochs=25,batch_size=32)

# make the prediction
y_pred = model.predict(X_test)
y_pred = (y_pred>0.5)

