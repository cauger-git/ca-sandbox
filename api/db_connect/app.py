import os
import json
import simplejson
from flask import Flask
from flask.json import jsonify
import cx_Oracle
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import String, Numeric

app = Flask(__name__)

def login_db():
    global TABLE_META
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    print("User: " + db_user)
    print("Pass: " + db_pass)
    db_string = "oracle://" + os.environ['DB_USER'] + ":" + os.environ['DB_PASS'] + "@stsorau.IC.GC.CA:1521/uat01ls"
    db_engine = create_engine(db_string)
    db_session = sessionmaker(bind=db_engine)
    #TABLE_META = MetaData(db_engine, schema="mini_spectra")
    return db_session()

@app.route('/')
def index():
    
    # Login to database
    db_session = login_db()

    return 'Connected to DB'

app.run(host='0.0.0.0', port=8080)
