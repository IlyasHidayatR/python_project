# In[]:
# make a heart disease prediction model with LSTM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# In[]:
# import dataset
dataset = pd.read_csv('heart.csv')
dataset.head()

# In[]:
# check the dataset information
dataset.info()

# In[]:
# check distribution of the target variable
sns.countplot(x='target',data=dataset)
plt.show()

# In[]:
# check the correlation between the features
plt.figure(figsize=(10,10))
sns.heatmap(dataset.corr(),annot=True)
plt.show()


# In[]:
# split the dataset into features and target
X = dataset.drop('target',axis=1)
y = dataset['target']

# In[]:
# split the dataset into training and testing dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# In[]:
# scale the features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# In[]:
# reshape the features
X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

# In[]:
# build the LSTM model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

model = Sequential()
model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1],1)))
model.add(Dropout(0.5))
model.add(LSTM(units=50,return_sequences=True))
model.add(LSTM(units=50))
model.add(Dense(units=1))

# In[]:
# compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# In[]:
# train the model
model.fit(X_train,y_train,epochs=100,batch_size=32)

# In[]:
# make the prediction
y_pred = model.predict(X_test)
y_pred = (y_pred>0.5)

# In[]:
# check the prediction
y_pred

# In[]:
# check the accuracy
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)
print(cm)
accuracy_score(y_test,y_pred)

# In[]:
# save the model
model.save('heart_disease.h5')