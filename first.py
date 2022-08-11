import pymysql
from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect, url_for, send_from_directory, render_template
import json

conn = pymysql(host='localhost', 
                user = 'host',
                password = '05020130lee@',
                db = 'Boards',
                charset = 'utf8')

curs = conn.cursor()

if conn.open:
    print('connected')

app = Flask(__name__)

@app.route('/test', methods =['POST'])
def postJsonHandler():
    print(request.is_json)
    content =request.get_json()
    print (content)
    id = content['id']
    print ("#####id:",id)
    sql = "select * from posttbl"
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    data = {'id' : 'yebin'}
    return json.dumps(data)

app.run(host = "192.168.0.11", port = 443)