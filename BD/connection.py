import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='654321',
                db='universidad'
            )
        except Error as ex:
            print("Error when trying to connect: {0}".format(ex))

    def listCourses(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                results = cursor.fetchall()
                return results
            except Error as ex:
                print("Error when trying to connect: {0}".format(ex))
