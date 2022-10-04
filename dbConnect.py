# vim dbConnect.py

import pymysql

def dbcon():
    conn = pymysql.connect(host='localhost', user='root', password='05020130lee@', db='test', charset='UTF8') # mysql 연결

    if conn.open: # DB 연결 여부 확인
        print('connected')
    return conn

def dbclose(conn):
    conn.close() # DB 연결 해제