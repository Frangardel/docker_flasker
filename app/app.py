from flask import Flask, jsonify
from sqlalchemy import create_engine
from datetime import datetime
from flask_restx import Api, Namespace, Resource, reqparse, inputs, fields

user = "schedulin"
passw = "MySQLIsFun"
host = "35.231.228.133"
database = "schedulin"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = host

@app.route('/')
def hello():
    return 'Hello again!'

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

@app.route('/users')
def get_users():
    connection = connect()
    select = """
        SELECT *
        FROM user
        WHERE deletion_date IS NULL
        LIMIT 10;"""
    result = connection.execute(select).fetchall()
    disconnect(connection)
    return jsonify({'result': [dict(row) for row in result]})

app.run()