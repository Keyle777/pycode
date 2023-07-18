
import pytesseract
from PIL import Image
from PIL import ImageGrab
import time


# 指定截图区域的中心坐标和宽度、高度
center_x = 938
center_y = 605
width = 330
height = 50

# 计算截图区域的左上角和右下角坐标
left = center_x - width // 2
top = center_y - height // 2
right = center_x + width // 2
bottom = center_y + height // 2

time.sleep(5)
# 截取屏幕指定区域的截图
im = ImageGrab.grab(bbox=(left, top, right, bottom))

# 保存截图为PNG格式的图片文件
im.save("screenshot.png")

text = pytesseract.image_to_string(Image.open("D:\\pycode\screenshot.png"),lang="eng")
print(text)