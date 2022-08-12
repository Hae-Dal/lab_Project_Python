import pymysql
from flask import Flask
import datetime, json

conn = pymysql.connect(host='localhost', user='root', password='05020130lee@', db='Boards', charset='utf8') # mysql 연결
curs = conn.cursor() # sql문을 입력할 cursor 생성

if conn.open: # DB 연결 여부 확인
    print('connected')
try:
    app = Flask(__name__) 
    # flask 메인 
    # __name__: 현재 이 파일을 실행하고 있는 파일의 이름이 들어감(원본과 같은 파일 일 경우 '__main__')

    @app.route('/test',methods=['POST','GET']) 
    # route() : 외부 웹브라우져에서 웹서버로 접근 시 해당 주소로 입력을 하게 되면 특정 함수가 실행되게 도와줌('/test': /test 주소에 접근하면 아래 함수 실행)
    def dbToWeb(): # DB에서 웹으로 데이터를 보내기위한 함수
            sql = "select * from posttbl" # DB에서 필요한 데이터 select하는 sql문
            curs.execute(sql) # sql문 실행
            rows = curs.fetchall() # select한 데이터 fetch (fetchall() : 모든 데이터 fetch)
            return json.dumps(rows, default=json_default) 
            # fetch한 데이터 json형식으로 변환 후 string으로 바꿔서 return
            # default : 에러가 났을 시에 실행

    def json_default(value): # DB 내 데이터 형식 중 JSON으로 변환 불가능한 형식이 있을때, STRING으로 바꿔줌
        if isinstance(value, datetime.date):
            return value.strftime('%Y-%m-%d') # strftime : 날짜, 시간을 string으로 변환ㅊ
        raise TypeError('not JSON serializable')

finally:
    app.run(host='0.0.0.0', port= 5000) # 웹서버 호스트, 포트 지정
    conn.close() # DB 연결 해제
    