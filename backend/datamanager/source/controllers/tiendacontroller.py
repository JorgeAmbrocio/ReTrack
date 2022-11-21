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