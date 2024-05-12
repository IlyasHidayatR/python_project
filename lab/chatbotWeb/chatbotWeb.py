# Make chatbot with cnn model and flask web server API
import numpy as np
import os
import sys
import json
import random
import time
import datetime
import flask
from latihData import bag_of_words, stem, tokenize, stemmer

# load intents.json
with open('intents.json') as file:
    data = json.load(file)

# load data.json
with open('data.json') as file:
    data = json.load(file)

# load model
model = tf.keras.models.load_model('model.h5')

# load words
words = data['words']

# load labels
labels = data['labels']

# load intents
intents = data['intents']

# define flask app
app = flask.Flask(__name__)

# define home route
@app.route('/')
def home():
    return flask.render_template('index.html')

# define chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # get message from client
    message = flask.request.form['message']
    # predict message
    results = model.predict([bag_of_words(message, words)])
    # get index of the highest value
    results_index = np.argmax(results)
    # get tag
    tag = labels[results_index]
    # get response
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    # return response to client
    return flask.jsonify(random.choice(responses))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)