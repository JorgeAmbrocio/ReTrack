from __main__ import app
from flask import Flask, request, jsonify, make_response
from controllers import pisocontroller

##### ROUTING FROM PISO

# GET ALL PISOS FROM TIENDA
@app.route('/tienda/<id>/piso', methods=['GET'])
def get_all_piso(id):
    response = pisocontroller.get_all_piso()
    return jsonify(response)

# GET ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<id_piso>', methods=['GET'])
def get_one_piso(id, id_piso):
    response = pisocontroller.get_one_piso(id_piso)
    return jsonify(response)

# CREATE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso', methods=['POST'])
def create_piso(id):
    body = request.get_json()
    try:
        response = pisocontroller.create_piso(body)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})

# UPDATE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<idpiso>', methods=['PUT'])
def update_piso(id, idpiso):
    body = request.get_json()
    try:
        response = pisocontroller.update_piso(idpiso, body)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})

# DELETE ONE PISO FROM TIENDA
@app.route('/tienda/<id>/piso/<id_piso>', methods=['DELETE'])
def delete_piso(id, id_piso):
    try:
        response = pisocontroller.delete_piso(id_piso)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})
    return jsonify(response)