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
    response = tiendacontroller.get_one_tienda(id)
    return jsonify(response)

# CREATE ONE TIENDA
@app.route('/tienda', methods=['POST'])
def create_tienda():
    body = request.get_json()
    try:
        response = tiendacontroller.create_tienda(body)
        return jsonify(response)
    except Exception as e:
        return jsonify({'msg': "{}".format(e), 'status': 500})

# UPDATE ONE TIENDA
@app.route('/tienda/<id>', methods=['PUT'])
def update_tienda(id):
    body = request.get_json()
    try:
        response = tiendacontroller.update_tienda(id, body)
        return jsonify(response)
    except Exception as e:
        return jsonify({'msg': "{}".format(e), 'status': 500})

# DELETE ONE TIENDA
@app.route('/tienda/<id>', methods=['DELETE'])
def delete_tienda(id):
    try:
        response = tiendacontroller.delete_tienda(id)
        return jsonify(response)
    except Exception as e:
        return jsonify({'msg': "{}".format(e), 'status': 500})