from flask import Flask, jsonify
from flask_cors import CORS

from constants import THEMES 


app = Flask(__name__)

CORS(app)

PORT = 5002

@app.route('/themes', methods=['GET'])
def get_exercises():
    response = jsonify(THEMES)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
