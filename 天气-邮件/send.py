import smtplib, requests, json
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from bs4 import BeautifulSoup
import time
from email.utils import formatdate

# 配置信息
config = {
    'host': "smtp.qq.com",  # 邮件服务器地址
    'user': "1059819521@qq.com",  # 发件人邮箱账号
    'pass': "vwknsxlvdaevbdgd",  # 发件人邮箱密码或授权码
    'sender': '1059819521@qq.com',  # 发件人邮箱
    'receivers': 'keyle192@gmail.com',  # 收件人邮箱
    'senderName': '波波',  # 发件人姓名
    'receiverName': '波波的Gmail邮箱'  # 收件人姓名
}

# 请求天气接口
url = 'https://weather.cma.cn/api/weather/view?stationid=57516'  # 重庆市气象站的天气接口
headers = {
    "Authorization": "APPCODE " + config['appcode'],
    "Content-Type": "application/json; charset=utf-8"
}
response = requests.get(url, headers=headers).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
daily = json.loads(response)['data']['daily'][0]
now = json.loads(response)['data']['now']

# 获取天气信息
high = daily['high']  # 最高温度
low = daily['low']  # 最低温度
dayText = daily['dayText']  # 天气情况
temperature = now['temperature']  # 当前温度
pressure = now['pressure']  # 当前压强
humidity = now['humidity']  # 当前湿度

# 配置邮件体
message = MIMEText('今日重庆天气：' + str(temperature) + '摄氏度' + '天气情况：' + str(dayText), 'plain', 'utf-8')
message['From'] = formataddr([config['senderName'], config['sender']])  # 发件人名称和邮箱地址
message['To'] = formataddr([config['receiverName'], config['receivers']])  # 收件人名称和邮箱地址
message['Subject'] = Header('柠檬心工作室每日天气预报', 'utf-8')  # 邮件主题
message['Date'] = formatdate(time.time(), localtime=True)

try:
    # 连接邮件服务器并发送邮件
    smtpObj = smtplib.SMTP()
    smtpObj.connect(config['host'], 587)  # 连接到QQ邮件服务器的587端口（TLS加密）
    smtpObj.login(config['user'], config['pass'])  # 登录QQ邮件服务器
    smtpObj.sendmail(config['sender'], config['receivers'], message.as_string())  # 发送邮件
    print("邮件发送成功")
except smtplib.SMTPException:
    print("发送邮件错误")