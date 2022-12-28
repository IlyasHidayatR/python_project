# make chatbot with transfer learning
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import json

# Load the pre-trained model from TensorFlow Hub
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Define the input and output
# load intents.json
with open('lab/Chatbot/intents.json') as file:
    data = json.load(file)

# define the input and output
# input
input = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        input.append(pattern)

# output
output = []
for intent in data['intents']:
    output.append(intent['responses'])

# Encode the input and output
input = model(input)
output = model(output)

# Calculate the cosine similarity between the input and output vectors
similarity = tf.matmul(input, output, transpose_b=True)

# Find the most similar output vector for each input vector
most_similar = tf.argmax(similarity, axis=1)

# Define the chatbot
def chatbot():
    # Get the input from the user
    user_input = input("Ask me something: ")
    
    # Encode the user input
    user_input = model([user_input])
    
    # Calculate the cosine similarity between the user input and the output vectors
    similarity = tf.matmul(user_input, output, transpose_b=True)
    
    # Find the most similar output vector
    most_similar = tf.argmax(similarity, axis=1)
    
    # Get the index of the most similar output vector
    most_similar = most_similar.numpy()[0]
    
    # Get the most similar output vector
    most_similar = output[most_similar]
    
    # Calculate the cosine similarity between the user input and the most similar output vector
    similarity = tf.matmul(user_input, most_similar, transpose_b=True)
    
    # Find the similarity score
    similarity = similarity.numpy()[0][0]
    
    # Print the similarity score
    print("Similarity score: ", similarity)
    
    # If the similarity score is less than 0.5, print "I don't understand"
    if similarity < 0.5:
        print("I don't understand")
    # Else, print the most similar output vector
    else:
        print(most_similar.numpy()[0])

# Run the chatbot
chatbot()

