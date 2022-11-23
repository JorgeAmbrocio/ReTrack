from contexts import retrackcontext
from mysql.connector import Error

# GET ALL PASILLOS
def get_all_pasillo():
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Pasillo"
    )

    # execute the query
    try:
        cursor.execute(query)
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pasillos = []
        for row in result:
            pasillo = dict(zip(headers, row))
            pasillos.append(pasillo)
        
        return {'msg': pasillos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# GET ONE PASILLO
def get_one_pasillo(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Pasillo WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pasillos = []
        for row in result:
            pasillo = dict(zip(headers, row))
            pasillos.append(pasillo)
        
        return {'msg': pasillos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# GET ALL PASILLOS BY TIENDA
def get_all_pasillo_by_tienda(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Pasillo WHERE idTienda = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pasillos = []
        for row in result:
            pasillo = dict(zip(headers, row))
            pasillos.append(pasillo)
        
        return {'msg': pasillos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# GET ONE PASILLO BY TIENDA
def get_one_pasillo_by_tienda(idTienda, idPasillo):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Pasillo WHERE id = %s AND idTienda = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (idPasillo, idTienda))
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pasillos = []
        for row in result:
            pasillo = dict(zip(headers, row))
            pasillos.append(pasillo)
        
        return {'msg': pasillos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# CREATE PASILLO
def create_pasillo(body):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "INSERT INTO Pasillo (nombre, cntSecciones, puntosLimitadores, idDireccion, idPiso) "
        "VALUES (%(nombre)s, %(cntSecciones)s, %(puntosLimitadores)s, %(idDireccion)s, %(idPiso)s) "
    )

    # execute the query
    try:
        cursor.execute(query, body)
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': "Pasillo creado correctamente", 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# UPDATE PASILLO
def update_pasillo(id, body):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "UPDATE Pasillo SET nombre = %(nombre)s, cntSecciones = %(cntSecciones)s, puntosLimitadores = %(puntosLimitadores)s, idDireccion = %(idDireccion)s, idPiso = %(idPiso)s "
        " WHERE id = %(id)s "
    )

    # execute the query
    try:
        cursor.execute(query, {**body, 'id': id})
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': "Pasillo actualizado correctamente", 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# DELETE PASILLO
def delete_pasillo(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "DELETE FROM Pasillo WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': "Pasillo eliminado correctamente", 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

