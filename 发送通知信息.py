import time
from pymongo.mongo_client import MongoClient
import requests, json
from bs4 import BeautifulSoup

config = {
    "appid": 'w6',
    "secret": '9a3',
    "template_id": 'mmlkiVj6L8hoHQKY6sL0'
}

def coon():
    uri = "mongodb+srv://root:Xingmimi221...@cluster0.ri0h7iy.mongodb.net/?retryWrites=true&w=majority"
    # 创建连接
    client = MongoClient(uri)
    return client

cursor = coon()
try:
    # 读取库
    db = cursor.user
    # 读取集合
    collection = db.user
    # 删除所有数据
    x = collection.delete_many({})       
except Exception as e:
    print(e)


host = 'https://api.weixin.qq.com/cgi-bin'
url = host + '/token?grant_type=client_credential&appid={appid}&secret={secret}'.format(
    appid=config['appid'], secret=config['secret'])
response = requests.post(url).content.decode('utf-8')
print(json.loads(response))
access_token = json.loads(response)['access_token']  # 获取token
# 请求发送消息接口

# 爬取当前天气信息
url = 'https://weather.cma.cn/api/weather/view?stationid=57516'
response = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
daily = json.loads(response)['data']['daily'][0]
now = json.loads(response)['data']['now']

high = daily['high']  # 最高温度
low = daily['low']  # 最低温度
dayText = daily['dayText']  # 天气情况
temperature = now['temperature']  # 当前温度
pressure = now['pressure']  # 压强
humidity = now['humidity']  # 湿度


def sendMessage(openId,nickName):
    data = {
        "touser": openId,
        "template_id": config['template_id'],
        "data": {
            "phrase2": {
                "value": "重庆"
            },
            "phrase3": {
                "value": dayText
            },
            "date1": {
                "value": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            },
            "character_string4": {
                "value": str(low) + '~' + str(high) + "°"
            },
            "thing5": {
                "value": "宝，记得随时关注天气信息哦"
            }
        }
    }
    url = host + '/message/subscribe/send?access_token={access_token}'.format(
        access_token=access_token)
    response = requests.post(url, json=data).content.decode('utf-8')
    print(json.loads(response),'------------------------>',nickName)


#查询数据库openId

# 查询所有文档
results = collection.find()

# 遍历结果
for result in results:
    print(result)


