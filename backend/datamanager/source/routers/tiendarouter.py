from __main__ import app
from flask import Flask, request, jsonify, make_response
from controllers import tiendacontroller

##### ROUTING FROM TIENDA

# GET ALL TIENDAS
@app.route('/tienda', methods=['GET'])
def get_all_tienda():
    response = tiendacontroller.get_all_tienda()
    return jsonify(response)

# GET ONE TIENDA
@app.route('/tienda/<id>', methods=['GET'])
def get_one_tienda(id):
    return jsonify({'message': 'GET ONE TIENDA'})

# CREATE ONE TIENDA
@app.route('/tienda', methods=['POST'])
def create_tienda():
    return jsonify({'message': 'CREATE ONE TIENDA'})

# UPDATE ONE TIENDA
@app.route('/tienda/<id>', methods=['PUT'])
def update_tienda(id):
    return jsonify({'message': 'UPDATE ONE TIENDA'})

# DELETE ONE TIENDA
@app.route('/tienda/<id>', methods=['DELETE'])
def delete_tienda(id):
    return jsonify({'message': 'DELETE ONE TIENDA'})