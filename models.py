# vim models.py

import pymysql
from dbConnect import dbcon, dbclose

class Stores():
    def get_all():                                                  # DB에 있는 데이터 전부 꺼내오는 함수
        conn = dbcon()                                              # db연결 함수
        curdic = conn.cursor(pymysql.cursors.DictCursor)            # sql문을 입력할 cursor 생성
        sql = "SELECT * FROM Post"                                  # sql문
        curdic.execute(sql)                                         # sql문 실행
        store_lists = curdic.fetchall()                             # 전부 fetch
        dbclose(conn)                                               # DB 연결 해제
        return store_lists                                          # fetch한 내용을 리턴
    
    def post_count():                                               # DB의 가장 마지막 postnum을 가져오는 함수
        conn = dbcon()
        curdic = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT postnum FROM Post order by postnum DESC limit 1"
        curdic.execute(sql)
        postnum = curdic.fetchone()
        dbclose(conn)
        return postnum['postnum']

    def get_likenum(postnum):                                       # likenum 숫자 가져오는 함수
        conn = dbcon()
        curdic = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT likenum FROM Post WHERE postnum=%s"
        curdic.execute(sql, (postnum))
        likenum = curdic.fetchone()                                 # fetchone : 딕셔너리 형태로 fetch
        dbclose(conn)
        return likenum['likenum']


class sendData():
    def sendtodb(name,title,contents,time):
        count = int(Stores.post_count()) + 1
        likenum = 0
        conn = dbcon()                                              # db연결 함수
        data = (count,name,title,contents,time,likenum)             # 데이터 튜플형식으로 변경
        curdic = conn.cursor()                                      # sql문을 입력할 cursor 생성
        sql = "INSERT INTO Post VALUES(%s,%s,%s,%s,%s,%s)"          # sql문
        curdic.execute(sql, data)                                   # sql문 실행
        conn.commit()                                               # 수정사항 반영
        dbclose(conn)                                               # DB 연결 해제
        return print("sendtodb OK")

    def upLike(postnum):                                            # 좋아요 버튼 클릭시 likenum 수 증가 함수
        likenum = Stores.get_likenum(postnum) + 1             
        conn = dbcon()
        curdic = conn.cursor()
        sql = "UPDATE Post SET likenum=%s WHERE postnum=%s"
        curdic.execute(sql, (likenum,postnum))
        conn.commit()
        dbclose(conn)
        return print("upLike : success")