from __main__ import app
from flask import Flask, request, jsonify, make_response
from controllers import pasillocontroller

##### ROUTING FROM PASILLO

# GET ALL PASILLOS FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo', methods=['GET'])
def get_all_pasillo(id, id_piso):
    response = pasillocontroller.get_all_pasillo()
    return jsonify(response)

# GET ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['GET'])
def get_one_pasillo(id, id_piso, id_pasillo):
    response = pasillocontroller.get_one_pasillo(id_pasillo)
    return jsonify(response)

# CREATE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo', methods=['POST'])
def create_pasillo(id, id_piso):
    body = request.get_json()
    try:
        response = pasillocontroller.create_pasillo(body)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})

# UPDATE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['PUT'])
def update_pasillo(id, id_piso, id_pasillo):
    body = request.get_json()
    try:
        response = pasillocontroller.update_pasillo(id_pasillo, body)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})

# DELETE ONE PASILLO FROM PISO
@app.route('/tienda/<id>/piso/<id_piso>/pasillo/<id_pasillo>', methods=['DELETE'])
def delete_pasillo(id, id_piso, id_pasillo):
    try:
        response = pasillocontroller.delete_pasillo(id_pasillo)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({'msg': "{}".format(e), 'status': 500})
    return jsonify(response)
