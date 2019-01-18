from app import app
from flask_cors import CORS
from flasgger import Swagger
from pymongo import MongoClient
import sqlite3
import configparser
import codecs
import os
import json
                                                                                                                                                                    
CORS(app)
Swagger(app)

env = 'development'

def get_config():
    script_dir = os.path.dirname(__file__)
    rel_path = "config.ini"
    abs_file_path = os.path.join(script_dir, rel_path)
    config = configparser.ConfigParser()
    config.optionxform = str  # 沒這行的話，Key會全部改成小寫…
    config.read_file(codecs.open(abs_file_path, "r", "utf8"))
    return config

def connect_mongoDB():
    config = get_config()
    host = config.get(env, 'IQC_HOST')
    port = int(config.get(env, 'IQC_PORT'))
    conn = MongoClient(host=host, port=port)
    return conn

def connect_sqlite(dbfile, sqlcmd):
    script_dir = os.getcwd()
    rel_path = dbfile
    abs_file_path = os.path.join(script_dir, 'app/', rel_path)
    conn = sqlite3.connect(abs_file_path)
    cursor = conn.cursor()
    result = cursor.execute(sqlcmd)
    items = []
    for row in result:
        for key in cursor.description:
            items.append({key[0]: value for value in row})
    json_string = json.dumps(items, indent=4, ensure_ascii=False)
    return json_string
