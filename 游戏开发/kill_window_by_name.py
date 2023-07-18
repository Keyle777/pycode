# 打开软件/关闭软件
from ctypes import *
import subprocess
# 打开指定程序
app=subprocess.Popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')

import pyautogui

# 等待5秒，关闭软件
pyautogui.sleep(5)
pyautogui.hotkey("alt","f4")
 

