import cv2
import numpy as np

# 读取图片a和图片b
img_a = cv2.imread(r'D:\pycode\img\a20230713105750.png')
img_b = cv2.imread(r'D:\pycode\img\bb.png')

# 获取图片b的宽度和高度
height, width, _ = img_b.shape

# 使用cv2.matchTemplate()函数进行图像匹配
result = cv2.matchTemplate(img_a, img_b, cv2.TM_CCOEFF_NORMED)

# 从匹配结果中找到最佳匹配位置的左上角坐标
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# 绘制匹配结果的矩形框
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(img_a, top_left, bottom_right, (0, 0, 255), 2)

# 显示匹配结果
print('图片b在图片a中的位置坐标为：', top_left)