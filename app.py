from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings', methods=['GET'])
def greetings():
    return jsonify({"message": "Hello, World!"})