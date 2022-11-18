from __main__ import app
from flask import Flask, request, jsonify, make_response

##### ROUTING FROM PASILLO

# GET ALL PASILLOS FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo', methods=['GET'])
def get_all_pasillo(id, id_piso):
    return jsonify({'message': 'GET ALL PASILLOS FROM PISO'})

# GET ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['GET'])
def get_one_pasillo(id, id_piso, id_pasillo):
    return jsonify({'message': 'GET ONE PASILLO FROM PISO'})

# CREATE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo', methods=['POST'])
def create_pasillo(id, id_piso):
    return jsonify({'message': 'CREATE ONE PASILLO FROM PISO'})

# UPDATE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['PUT'])
def update_pasillo(id, id_piso, id_pasillo):
    return jsonify({'message': 'UPDATE ONE PASILLO FROM PISO'})

# DELETE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['DELETE'])
def delete_pasillo(id, id_piso, id_pasillo):
    return jsonify({'message': 'DELETE ONE PASILLO FROM PISO'})
