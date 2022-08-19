#vim app.py

from flask  import Flask, json
import datetime
from models import Stores

app = Flask(__name__)

@app.route('/dbtoweb')
# route() : 외부 웹브라우져에서 웹서버로 접근 시 해당 주소로 입력을 하게 되면 특정 함수가 실행되게 도와줌('/test': /test 주소에 접근하면 아래 함수 실행)
def dbToWeb(): # DB에서 웹으로 데이터를 보내기위한 함수
    data = Stores.get_all()
    return json.dumps(data, default=json_default)

def json_default(value): # DB 내 데이터 형식 중 JSON으로 변환 불가능한 형식이 있을때, STRING으로 바꿔줌
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d') # strftime : 날짜, 시간을 string으로 변환ㅊ
    raise TypeError('not JSON serializable')

#@app.route('/andtodb',methods=['POST','GET']) 
    



    