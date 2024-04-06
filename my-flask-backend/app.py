from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()  # Get input data from the request
    input_data = data.get('input')  # Extract the input value
    # Process the input data (example: convert to uppercase)
    processed_data = input_data.upper()

    with open('blockchain/formdata.json','w') as f:
        json.dump({'descr': processed_data}, f)

    return jsonify({'processed': processed_data})

@app.route('/api/data', methods=['GET'])
def get_data():
    # Open the JSON file
    with open('blockchain/bcdata.json') as file:
        # Read the JSON data
        json_data = json.load(file)
    return jsonify(json_data)



if __name__ == '__main__':
    app.run(debug=True)
