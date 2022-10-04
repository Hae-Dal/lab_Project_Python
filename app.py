#vim app.py

from inspect import _void
from flask  import Flask, json, request
import datetime
from models import Stores, sendData


app = Flask(__name__)

@app.route('/dbtoweb', methods=['POST','GET'])
def dbToWeb():                                                                                  # DB에서 웹으로 데이터를 보내기위한 함수 
    data = Stores.get_all()                                                                     # models.py의 Stores클래스 내의 get_all함수 실행
    return json.dumps(data, default=json_default, ensure_ascii=False)                           # json 형식으로 인코딩 후 String으로 변환해서 리턴

def json_default(value):                                                                        # DB 내 데이터 형식 중 JSON으로 변환 불가능한 형식이 있을때, STRING으로 바꿔줌
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')                                                       # strftime : 날짜, 시간을 string으로 변환
    raise TypeError('not JSON serializable')

@app.route('/sendserver', methods=['POST','GET'])
def toDB():                                                                                     # DB에 저장
    title = request.json['title']                                                               # json형태의 키값중 'title'의 값을 리턴
    contents = request.json['contents']                                                         # json형태의 키값중 'contents'의 값을 리턴
    userName = request.json['userName']                                                         # json형태의 키값중 'userName'의 값을 리턴
    time = request.json['time']                                                                 # json형태의 키값중 'time'의 값을 리턴
    sendData.sendtodb(userName,title,contents,time)                                             # models.py의 sendData클래스 내의 sendtodb함수 실행
    return "Success"

@app.route("/likeup", methods=['POST','GET'])
def upLike():
    postnum = request.form['postnum']
    sendData.upLike(int(postnum))
    return "Success"
    