# -*- coding: utf-8 -*-
 
from PyQt5.QtWidgets import QApplication
import win32gui
from numpy import array,uint8,ndarray
from datetime import datetime
import os
import cv2
import numpy as np
import re
import pyautogui as p
from ctypes import *
import subprocess

# 直接写一个类，方便以后使用
class Screen:
    def __init__(self, win_title=None, win_class=None, hwnd=None):
        self.app = QApplication(['WindowCapture'])
        self.screen = QApplication.primaryScreen()
        self.bind(win_title, win_class, hwnd)

    def bind(self, win_title=None, win_class=None, hwnd=None):
        '可以直接传入句柄，否则就根据class和title来查找，并把句柄做为实例属性 self._hwnd'
        if not hwnd:
            self._hwnd = win32gui.FindWindow(win_class, win_title)
        else:
            self._hwnd = hwnd

    def capture(self, savename='', quality=100):
        '截图方法，在窗口为 1920 x 1080 大小下，最快速度25ms (grabWindow: 17ms, to_cvimg: 8ms)'
        def to_cvimg(pix):
            '将self.screen.grabWindow 返回的 Pixmap 转换为 ndarray，方便opencv使用'
            qimg = pix.toImage()
            temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
            temp_shape += (4,)
            ptr = qimg.bits()
            ptr.setsize(qimg.byteCount())
            result = array(ptr, dtype=uint8).reshape(temp_shape)
            return result[..., :3]
        self.pix = self.screen.grabWindow(self._hwnd)
        self.img = to_cvimg(self.pix)
        if savename:
            self.pix.save(savename, quality=quality)
        return self.img
 
def positionIcon(img_a_url,img_b_url):
    # 读取图片a和图片b
    img_a = cv2.imread(img_a_url)
    img_b = cv2.imread(img_b_url)

    # 获取图片b的宽度和高度
    height, width, _ = img_b.shape

    # 使用cv2.matchTemplate()函数进行图像匹配
    result = cv2.matchTemplate(img_a, img_b, cv2.TM_CCOEFF_NORMED)

    # 从匹配结果中找到最佳匹配位置的左上角坐标
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 判断是否找到了匹配的坐标
    if max_val > 0.8:
        top_left = max_loc
        # 返回匹配的坐标
        return top_left
    else:
        # 没有找到匹配的坐标，返回None
        return None

def capture_and_click(title, img_url):
    # 截图并获取给定图标在屏幕中的坐标
    screen = Screen(win_title=title)
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    dir_path = os.path.join(os.getcwd(), "img")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = f"{title}_{now}.png"
    file_path = os.path.join(dir_path, file_name)
    screen.capture(file_path)
    top_left = positionIcon(file_path, img_b_url=img_url)
    if result is None:
        return None
    x, y = top_left
    # 移动鼠标并点击
    p.moveTo(x, y, duration=0.1526)
    p.click()
    # 删除图片，防止图片过多
    os.remove(file_path)

def type_string(string,time=0):
    for char in string:
        p.press(char)


if __name__ == '__main__':
    # 截图的程序名称
    title = "Desktop"
    # 打开指定程序
    app=subprocess.Popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
    p.sleep(60)
    p.click()
    # 等待进入大厅
    p.sleep(30)

    # 获取选择模式按钮的图片位置移动并点击，等待一段时间
    capture_and_click(title, 'xxx')

    # 选取模式图片位置移动并点击，等待一段时间
    capture_and_click(title, 'xxx')
    p.hotkey('esc')
    # 获取开始按钮的图片位置移动并点击，等待一段时间
    capture_and_click(title, 'xxx')
    # 等在进入选人页面
    p.sleep(15)
    while True:
        # 循环截图比对看是否已经到了加载页面
        result = capture_and_click(title, 'D:\\pycode\img\\bb.png')
        if result is not None:
            break
    p.sleep(20)
    # 进行选择武器套装
    capture_and_click(title, 'xxx')
    p.sleep(15)
    # 使人物后退并且点击鼠标左键进行开枪
    while True:
        # 模拟按下键盘上的'W'键
        p.press(keys='s',presses=2)
        p.click(clicks=3)
        # 等待2秒钟
        time.sleep(2)
        # 检测此时比分是否已经到达
        result = capture_and_click(title, 'D:\\pycode\img\\bb.png')
        if result is not None:
            break
    p.sleep(5)
    p.hotkey('esc')
    p.hotkey('enter')

    # 重新点击开始 第二次循环

    capture_and_click(title, 'xxx')
    # 等在进入选人页面
    p.sleep(15)
    while True:
        # 循环截图比对看是否已经到了加载页面
        result = capture_and_click(title, 'D:\\pycode\img\\bb.png')
        if result is not None:
            break
    p.sleep(20)
    # 进行选择武器套装
    capture_and_click(title, 'xxx')
    p.sleep(15)
    # 使人物后退并且点击鼠标左键进行开枪
    while True:
        # 模拟按下键盘上的'W'键
        p.press(keys='s',presses=2)
        p.click(clicks=3)
        # 等待2秒钟
        time.sleep(2)
        # 检测此时比分是否已经到达
        result = capture_and_click(title, 'D:\\pycode\img\\bb.png')
        if result is not None:
            break
    p.sleep(5)
    p.hotkey('esc')
    p.hotkey('enter')

# 执行循环体，然后等人物到达一定等级后，选择结束游戏进程
# time.sleep(5)
# pyautogui.hotkey("alt","f4")