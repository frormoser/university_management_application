import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
load_dotenv()


host = os.getenv('MYSQL_HOST')
db = os.getenv('MYSQL_DB')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')

print(user)


class DAO():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                db=db
            )
        except Error as ex:
            print("Error when trying to connect: {0}".format(ex))

    def listCourses(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")
                results = cursor.fetchall()
                return results
            except Error as ex:
                print("Error when trying to connect: {0}".format(ex))
