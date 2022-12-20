# In[]:
# sentimen analisis twitter dengan lstm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# In[]:
# import dataset twitter tweet.csv
dataset = pd.read_csv('tweet.csv')
dataset.head()

# In[]:
# menghapus kolom yang tidak diperlukan
dataset = dataset.drop(['Date','User','Polarity'],axis=1)
dataset.head()

# In[]:
# menghapus data yang kosong
dataset = dataset.dropna()
dataset.head()

# In[]:
# menghapus data yang duplikat
dataset = dataset.drop_duplicates()
dataset.head()

# In[]:
# cleaning data
def cleaning_text(text):
    text = re.sub(r'@[A-Za-z0-9]+','',text)
    text = re.sub(r'#','',text)
    text = re.sub(r'RT[\s]+','',text)
    text = re.sub(r'https?:\/\/\S+','',text)
    return text

dataset['Tweet'] = dataset['Tweet'].apply(cleaning_text)
dataset.head()

# In[]:
# menghapus stopwords
def remove_stopwords(text):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    text = stopword.remove(text)
    return text

dataset['Tweet'] = dataset['Tweet'].apply(remove_stopwords)
dataset.head()

# In[]:
# stemming
def stemming_text(text):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = stemmer.stem(text)
    return text

dataset['Tweet'] = dataset['Tweet'].apply(stemming_text)
dataset.head()

# In[]:
# mengubah data menjadi angka negatif, netral, positif
def change_to_number(text):
    if text == 'Negative':
        return 0
    elif text == 'Neutral':
        return 1
    else:
        return 2

dataset['Sentiment'] = dataset['Sentiment'].apply(change_to_number)
dataset.head()

# In[]:
# lakukan tokenisasi
def tokenisasi(text):
    return text.split()

dataset['Tweet'] = dataset['Tweet'].apply(tokenisasi)
dataset.head()

# In[]:
# membuat corpus
corpus = []
for i in range(len(dataset)):
    for j in range(len(dataset['Tweet'][i])):
        corpus.append(dataset['Tweet'][i][j])


# In[]:
# membuat dictionary
word_index = {}
for i in range(len(corpus)):
    if corpus[i] not in word_index:
        word_index[corpus[i]] = len(word_index)

# In[]:
# membuat data training dan data testing
X = dataset['Tweet']
y = dataset['Sentiment']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# In[]:
# membuat model
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer

max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_train = pad_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)
X_test = pad_sequences(X_test)

embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim,input_length = X_train.shape[1]))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())


# In[]:
# training model 
batch_size = 32
model.fit(X_train, to_categorical(y_train), epochs = 7, batch_size=batch_size, verbose = 2)

# In[]:
# testing model dan menampilkan hasilnya
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred,axis=1)
y_test = np.array(y_test)
print(classification_report(y_test, y_pred))

# In[]:
# visualisasi akurasi
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print('Akurasi : ',accuracy)

# In[]:
# visualisasi loss
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)


