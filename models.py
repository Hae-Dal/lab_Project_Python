# vim models.py

import pymysql

class Stores():
    def get_all(): # DB에 있는 데이터 전부 꺼내오는 함수
        conn = pymysql.connect(host='localhost', user='root', password='05020130lee@', db='Boards', charset='utf8') # mysql 연결
        if conn.open: # DB 연결 여부 확인
            print('connected')
        
        curdic = conn.cursor(pymysql.cursors.DictCursor) # sql문을 입력할 cursor 생성
        sql = "SELECT * FROM posttbl" # sql문
        curdic.execute(sql) # sql문 실행
        
        store_lists = curdic.fetchall() # 전부 fetch
        conn.close() # DB 연결 해제
        return store_lists # fetch한 내용을 리턴
        