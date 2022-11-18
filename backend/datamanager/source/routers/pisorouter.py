from __main__ import app
from flask import Flask, request, jsonify, make_response

##### ROUTING FROM PISO

# GET ALL PISOS FROM TIENDA
@app.route('/tienda/<id>/piso', methods=['GET'])
def get_all_piso(id):
    return jsonify({'message': 'GET ALL PISOS FROM TIENDA'})

# GET ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<id_piso>', methods=['GET'])
def get_one_piso(id, id_piso):
    return jsonify({'message': 'GET ONE PISO FROM TIENDA'})

# CREATE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso', methods=['POST'])
def create_piso(id):
    return jsonify({'message': 'CREATe ONE PISO FROM TIENDA'})

# UPDATE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<id_piso>', methods=['PUT'])
def update_piso(id, id_piso):
    return jsonify({'message': 'UPDATE ONE PISO FROM TIENDA'})

# DELETE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<id_piso>', methods=['DELETE'])
def delete_piso(id, id_piso):
    return jsonify({'message': 'DELETE ONE PISO FROM TIENDA'})