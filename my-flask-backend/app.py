from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS with default settings for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
