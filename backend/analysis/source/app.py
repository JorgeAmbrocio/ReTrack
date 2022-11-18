import json
import sys
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# FUNCTION TO TEST IF THE API IS WORKING
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API analysis is working!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7767)