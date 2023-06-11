import os
from flask import Flask
from peewee import MySQLDatabase, IntegerField

MYSQL_ROOT_USER = os.getenv('MYSQL_ROOT_USER')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
MYSQL_ROOT_HOST = os.getenv('MYSQL_ROOT_HOST')
MYSQL_ROOT_PORT = os.getenv('MYSQL_ROOT_PORT')
MYSQL_ROOT_DB = os.getenv('MYSQL_ROOT_DB')
FLASK_APP_PORT = os.getenv('FLASK_APP_PORT')

db = MySQLDatabase(database=MYSQL_ROOT_DB, user=MYSQL_ROOT_USER, password=MYSQL_ROOT_PASSWORD,
                   host=MYSQL_ROOT_HOST, port=int(MYSQL_ROOT_PORT))

app = Flask(__name__)
app.run(host='0.0.0.0', port=int(FLASK_APP_PORT))

"""Function to test the functionality of the API"""
@app.route("/")
def index():
    return "This is Home Page"

"""Function to retrieve all users from the MySQL database"""
@app.route('/users', methods=["GET"])
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM USERS")
    data = cursor.fetchall()
    db.close()
    return "Users are :\n %s " % data
