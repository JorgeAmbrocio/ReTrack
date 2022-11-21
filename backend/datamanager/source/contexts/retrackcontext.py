import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# load enviroment
load_dotenv()

# Connect to the database
def define_connection():
    return mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

# test the connection
def test_connection():
    try:
        connection = define_connection()
        print('Connection to MySQL database successful')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)
        
        return False
    else:
        connection.close()
        return True