#vim app.py

from inspect import _void
from flask  import Flask, json, request
import datetime
from models import Stores, sendData

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def helloWorld():
    return "helloWorld"

@app.route('/dbtoweb', methods=['POST'])
# route() : 외부 웹브라우져에서 웹서버로 접근 시 해당 주소로 입력을 하게 되면 특정 함수가 실행되게 도와줌('/test': /test 주소에 접근하면 아래 함수 실행)
def dbToWeb(): # DB에서 웹으로 데이터를 보내기위한 함수
    data = Stores.get_all() # models.py의 Stores클래스 내의 get_all함수 실행
    return json.dumps(data, default=json_default) # json 형식으로 인코딩 후 String으로 변환해서 리턴

def json_default(value): # DB 내 데이터 형식 중 JSON으로 변환 불가능한 형식이 있을때, STRING으로 바꿔줌
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d') # strftime : 날짜, 시간을 string으로 변환
    raise TypeError('not JSON serializable')

@app.route('/sendserver', methods=['POST','GET'])
def toDB(): # DB에 저장
    id = request.json['userID'] # json형태의 키값중 'userID'의 값을 리턴
    password = request.json['userPassword'] # json형태의 키값중 'userPassword'의 값을 리턴
    name = request.json['userName'] # json형태의 키값중 'userName'의 값을 리턴
    sendData.sendtodb(id,password,name) # models.py의 sendData클래스 내의 sendtodb함수 실행
    return "Success"