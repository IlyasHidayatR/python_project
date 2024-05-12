from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from threading import Thread
import numpy as np
import json
import nltk
import schedule
import time
import random
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import mysql.connector


nltk.download('punkt')
factory = StemmerFactory()
stemmer = factory.create_stemmer()

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(" ".join(wrds))
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# Split data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(
    docs_x, docs_y, test_size=0.2, random_state=40)

vectorizer = CountVectorizer()
mlp_model = MLPClassifier(hidden_layer_sizes=(
    50, 30), max_iter=500, activation='relu', solver='adam', random_state=50, alpha=0.01, learning_rate='invscaling', learning_rate_init=0.01, batch_size=32, shuffle=True)

# Buat pipeline untuk menggabungkan proses preprocessing dan model
model = make_pipeline(vectorizer, StandardScaler(with_mean=False), mlp_model)

# Training loop
model.fit(X_train, y_train)

# akurasi model pada data latih
y_pred = model.predict(X_train)
accuracy = accuracy_score(y_train, y_pred)
print(f"Accuracy on training data: {accuracy * 100:.2f}%")

# Evaluasi model pada data uji
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test data: {accuracy * 100:.2f}%")

print("Training completed!")


def preprocess_input(input_text):
    input_text = input_text.lower()
    input_words = nltk.word_tokenize(input_text)
    input_text = " ".join([stemmer.stem(word) for word in input_words])
    return input_text


def get_intent_tag(input_text, model):
    input_text = preprocess_input(input_text)
    results = model.predict_proba([input_text])[0]
    results_index = np.argmax(results)
    tag = model.classes_[results_index]
    results = results[results_index]
    return tag, results


def get_response(tag, data, results):
    for intent in data["intents"]:
        if intent['tag'] == tag and intent['responses'] and results > 0.7:
            return random.choice(intent['responses'])
    return "Maaf, saya tidak mengerti pertanyaan Anda."


user_tokens = {
    "user1": "token_user1",
    "user2": "token_user2",
    # ... tambahkan akun pengguna dan token sesuai kebutuhan Anda
}


# def create_db_connection():
#     return mysql.connector.connect(
#         host='your_mysql_host',
#         user='your_mysql_user',
#         password='your_mysql_password',
#         database='your_mysql_database'
#     )


# Fungsi untuk memeriksa keberadaan dan kecocokan token


def verify_token(request):
    provided_token = request.headers.get("Authorization")

    if not provided_token or provided_token not in user_tokens.values():
        abort(401, "Unauthorized - Invalid Token")

    # buat koneksi ke database
    # conn = create_db_connection()
    # cursor = conn.cursor()

    # # Cek API Token dari database berdasarkan token yang diberikan
    # cursor.execute(
    #     "SELECT api_token FROM users WHERE api_token = %s", (provided_token,))
    # result = cursor.fetchone()

    # # tutup koneksi ke database
    # cursor.close()
    # conn.close()

    # if not result:
    #     abort(401, "Unauthorized - Invalid Token")

    # # dapatkan token pengguna dari hasil query
    # user_token = result[0]

    # # dapatkan token pengguna dari header
    # if provided_token != user_token:
    #     abort(401, "Unauthorized - Invalid Token")

    # return True

# Dekorator untuk memeriksa token sebelum memproses permintaan


def token_required(func):
    def wrapper(*args, **kwargs):
        verify_token(request)
        return func(*args, **kwargs)
    return wrapper

# Fungsi untuk memperbarui model (dipanggil setiap 24 jam)


def update_model():
    global model
    # Lakukan proses pembaharuan model di sini
    print("Model updated successfully.")


# Jalankan fungsi update_model() setiap 24 jam
schedule.every(24).hours.do(update_model)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Fungsi utama untuk menjalankan aplikasi Flask


def run_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/chat', methods=['POST'])
    @token_required
    def chat():
        user_input = request.json.get('user_input')
        if user_input.lower() == "quit":
            responses = "Bot: Goodbye!"
            # Code to stop the Flask application if needed
            # shutdown = request.environ.get('werkzeug.server.shutdown')
        else:
            tag, results = get_intent_tag(user_input, model)
            responses = get_response(tag, data, results)
        return jsonify({'responses': responses})

    if __name__ == '__main__':
        Thread(target=run_schedule).start()
        app.run(host='10.100.20.10', port=5000, debug=True)


# jalankan aplikasi Flask
run_app()
