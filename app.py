from flask import Flask, render_template, request
from Intelli_bot import chat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_handler():
    user_input = request.form['user_input']
    response = chat(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
