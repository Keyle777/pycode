# 天气信息更新系统pipi
import smtplib, requests, json
from bs4 import BeautifulSoup
import telebot
import schedule
import time

# 定义机器人信息
bot = telebot.TeleBot('6118674008:AAGyuJQvrS8ZnKNgb_FqRX-bMrLVOZeDnNA')
chat_id = '5899501226'

# 南京、新蔡县天气信息
urls = ['https://weather.cma.cn/api/weather/view?stationid=57293', 'https://weather.cma.cn/api/weather/view?stationid=58238']
tag = ''

# 预警颜色和表情符号对应关系
alert_emoji = {
    "红色": "🔴",
    "橙色": "🟠",
    "黄色": "🟡",
    "蓝色": "🔵",
    "白色": "⚪️"
}

def send_weather_info():
    global tag

    # 清空tag，避免重复添加信息
    tag = ''

    for i, url in enumerate(urls):
        response = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(response, "html.parser")
        city_name = json.loads(response)['data']['location']['name']
        daily = json.loads(response)['data']['daily']  # 未来几天的天气预报
        now = json.loads(response)['data']['now']

        high = daily[0]['high']  # 最高温度
        low = daily[0]['low']  # 最低温度
        dayText = daily[0]['dayText']  # 天气情况
        temperature = now['temperature']  # 当前温度
        pressure = now['pressure']  # 压强
        humidity = now['humidity']  # 湿度

        # 生成城市天气信息
        city_weather = f"*{city_name}*：\n\n今日气温：{low}-{high}℃，{dayText}。\n现在温度：{temperature}℃，压强：{pressure}百帕，湿度：{humidity}%。\n\n"
        tag += city_weather

        # 添加小提示
        if "雨" in dayText:
            tip = "出门注意不要忘记带雨伞哦 ☔️"
        elif "晴" in dayText:
            tip = "今天天气不错，可以出门去逛逛 🌞"
        elif "雪" in dayText:
            tip = "出门要穿暖和，注意路面湿滑 ❄️"
        else:
            tip = "今天的天气有些特别，出门前多留意天气变化哦 🌦"
        tag += f"{tip}\n\n---\n\n"

        # 加入未来几天的天气预报
        tag += f"\n未来几天的天气预报：\n"
        for j in range(1, len(daily)):
            day = daily[j]
            date = day['date']
            high = day['high']
            low = day['low']
            dayText = day['dayText']
            nightText = day['nightText']
            tag += f"`{date}`：{dayText}转{nightText}，最高气温：{high}℃，最低气温：{low}℃。\n"

        # 处理预警信息
        alert_list = json.loads(response)['data']['alarm']
        for alert in alert_list:
            alert_title = alert['title']  # 预警标题
            alert_color = alert['signallevel']  # 预警颜色
            alert_emoji_str = alert_emoji.get(alert_color, "")  # 获取预警颜色对应的表情符号
            alert_text = f"*{alert_title}* {alert_emoji_str}\n"  # 将预警标题和表情符号组合成文本
            tag += alert_text

    # 发送消息到Telegram
    bot.send_message(chat_id, tag, parse_mode="Markdown")

# 设定定时任务
schedule.every().hour.do(send_weather_info)

# 执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)