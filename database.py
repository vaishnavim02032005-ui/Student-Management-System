import mysql.connector

def connect_db():
    connection = mysql.connector.connect(host="localhost", user="root", password="020305", database="student_db")
    return connection