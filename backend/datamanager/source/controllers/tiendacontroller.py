from contexts import retrackcontext
from mysql.connector import Error

# GET ALL TIENDAS
def get_all_tienda():
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Tienda"
    )

    # execute the query
    try:
        cursor.execute(query)
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        tiendas = []
        for row in result:
            tienda = dict(zip(headers, row))
            tiendas.append(tienda)
        
        return {'msg': tiendas, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# GET ONE TIENDA
def get_one_tienda(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "SELECT * FROM Tienda WHERE id = %s"
    )

    # execute the query
    try:
        cursor.execute(query, (id,))
        headers = [i[0] for i in cursor.description]
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        # create a list of dictionaries
        tiendas = []
        for row in result:
            tienda = dict(zip(headers, row))
            tiendas.append(tienda)
        
        return {'msg': tiendas, 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}
    
# CREATE ONE TIENDA
def create_tienda(body):

    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "INSERT INTO Tienda (nombre) VALUES (%(nombre)s)"
    )

    try:
        cursor.execute(query, body)
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': 'Tienda creada', 'status': 201}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# UPDATE ONE TIENDA
def update_tienda(id, body):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "UPDATE Tienda SET nombre = %s WHERE id = %s"
    )

    try:
        cursor.execute(query, (body.get('nombre'), id))
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': 'Tienda actualizada', 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}

# DELETE ONE TIENDA
def delete_tienda(id):
    # create a new connection
    connection = retrackcontext.define_connection()
    cursor = connection.cursor()

    query = (
        "DELETE FROM Tienda WHERE id = %s"
    )

    try:
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

        return {'msg': 'Tienda eliminada', 'status': 200}
    except Error as e:
        connection.close()
        print(e)
        return {'msg': "{}".format(e), 'status': 500}