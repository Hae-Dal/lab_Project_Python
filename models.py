# vim models.py

import pymysql

class Stores():
    def get_all():
        conn = pymysql.connect(host='localhost', user='root', password='05020130lee@', db='Boards', charset='utf8') # mysql 연결
        if conn.open: # DB 연결 여부 확인
            print('connected')
        
        curdic = conn.cursor(pymysql.cursors.DictCursor) # sql문을 입력할 cursor 생성
        sql = "SELECT * FROM posttbl"
        curdic.execute(sql)
        
        store_lists = curdic.fetchall()
        conn.close() # DB 연결 해제
        return store_lists
        