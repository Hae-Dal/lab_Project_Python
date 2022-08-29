# vim models.py

import pymysql
from dbConnect import dbcon, dbclose

class Stores():
    def get_all(): # DB에 있는 데이터 전부 꺼내오는 함수
        conn = dbcon() # db연결 함수
        curdic = conn.cursor(pymysql.cursors.DictCursor) 
        # sql문을 입력할 cursor 생성
        sql = "SELECT * FROM posttbl" # sql문
        curdic.execute(sql) # sql문 실행
        
        store_lists = curdic.fetchall() # 전부 fetch
        dbclose(conn) # DB 연결 해제
        return store_lists # fetch한 내용을 리턴

class sendData():
    def sendtodb(id,postnum,posttitle,postcontents,postdate,postvisit,postlike):
        conn = dbcon() # db연결 함수
        data = (id,postnum,posttitle,postcontents,postdate,postvisit,postlike) 
        # 데이터 튜플형식으로 변경
        curdic = conn.cursor() # sql문을 입력할 cursor 생성
        sql = "INSERT INTO posttbl VALUES(%s,%d,%s,%s,%s,%d,%d)" # sql문
        curdic.execute(sql, data) # sql문 실행
        conn.commit() # 수정사항 반영
        dbclose(conn) # DB 연결 해제
        return print("sendtodb OK")