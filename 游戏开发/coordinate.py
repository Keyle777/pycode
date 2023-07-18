# 获取坐标
import datetime
import aircv as ac
import pyautogui as p
# 获取坐标的工具类
class getCoordinates:
    def __init__(self):
        last_pos= p.position()
        try:
            while True:
                new_pos=p.position()
                if last_pos!=new_pos:
                    print(new_pos)
                    last_pos=new_pos
        except KeyboardInterrupt:
            print("\nExit.")
# 执行获取坐标
process = getCoordinates()