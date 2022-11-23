from contexts import retrackcontext
from mysql.connector import Error

# GET ALL PISOS
def get_all_piso():
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Piso"
    )

    # execute the query
    try:
        cursor.execute(query)
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pisos = []
        for row in result:
            piso = dict(zip(headers, row))
            pisos.append(piso)
        
        return {'msg': pisos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# GET ONE PISO
def get_one_piso(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Piso WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        pisos = []
        for row in result:
            piso = dict(zip(headers, row))
            pisos.append(piso)
        
        return {'msg': pisos, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# CREATE ONE PISO
def create_piso(data):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "INSERT INTO Piso (nombre, idTienda) VALUES (%s, %s)"
    )

    # execute the query
    try:
        cursor.execute(query, (data['nombre'], data['idTienda']))
        connection.commit()

        cursor.close()
        connection.close()

        return {'msg': 'Piso creado correctamente', 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# UPDATE ONE PISO
def update_piso(id, data):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "UPDATE Piso SET nombre = %s,idTienda = %s WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (data['nombre'], data['idTienda'], id))
        connection.commit()

        cursor.close()
        connection.close()

        return {'msg': 'Piso actualizado correctamente', 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# DELETE ONE PISO
def delete_piso(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "DELETE FROM Piso WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        connection.commit()

        cursor.close()
        connection.close()

        return {'msg': 'Piso eliminado correctamente', 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}