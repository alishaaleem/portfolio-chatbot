from flask import Flask, send_from_directory, jsonify, request
from transformers import pipeline
import torch
import tensorflow as tf

app = Flask(__name__)

# Load a pre-trained NLP model
# nlp = pipeline("question-answering")
Q_AND_A = {
    "What is your name?": "My name is Alisha Anjum Aleem.",
    "What do you do?": "I am a seasoned software engineer with experience in various technologies.",
    "What are your skills?": "I have skills in Angular, Python, AWS, and more.",
    "What are your recent projects?": "I recently worked on building a chatbot with Angular and Flask."
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question')
    # context = data.get('context', "I am a chatbot here to answer your questions about Alisha.")
    # response = nlp(question=question, context=context)
    # answer = response['answer']

    # Find the answer in the predefined Q&A dictionary
    answer = Q_AND_A.get(question, "Sorry, I don't have an answer to that question.")
    return jsonify({'answer': answer})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
