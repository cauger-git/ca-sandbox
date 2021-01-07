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
    db_string = "oracle://" + os.environ['DB_USER'] + ":" + os.environ['DB_PASS'] + "@stsorau.IC.GC.CA:1521/uat01ls"
    db_engine = create_engine(db_string)
    db_session = sessionmaker(bind=db_engine)
    TABLE_META = MetaData(db_engine, schema="EMC")
    return db_session()

@app.route('/')
def index():
    
    # Login to database
    db_session = login_db()

    # Map the first 3 columns of the TX_RES_TAB table
    tx_res_tab = Table('TX_RES_TAB', TABLE_META, 
                            Column('TX_RES_ID', Numeric, nullable=False),
                            Column('ACD_ACD_ID', Numeric, nullable=True),
                            Column('TX_RES_STATE', String, nullable=True))
    
    # Count the rows
    count = db_session.query(tx_res_tab).count()

    result = "Table TX_RES_COUNT has " + count + " rows" 

    #print("Table has " + str(results) + " rows")

    return result
