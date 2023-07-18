# 自动操作
import aircv as ac
import pyautogui as p
#截取图片bb
def getSd(self):
    #region表示需要在屏幕中截取的位置，左上角和右下角的x，y坐标
    # region参数的值(100, 100, 100, 100)表示要捕获的区域的左上角坐标为(100, 100)
    # 宽度和高度均为100，因此捕获的截图包含了屏幕上从(100, 100)到(200, 200)的像素
    img = p.screenshot(region=[1078, 1035, 40, 40])
    #保存到本地
    img.save("img/bb.png")
    return None

 #匹配两张图片以0.7的相似度，如果匹配不到会返回空值 ac是我们上面引入的依赖
def matcha(self, bb, aa):
    yuan = ac.imread(bb)
    mubi = ac.imread(aa)
    result = ac.find_template(yuan, mubi, 0.7)  # 0.7相似度
    if (result != None):
        p.moveTo(1610, 22, duration=0.3)
        p.click()
        p.sleep(1)
        p.moveTo(954, 773, duration=0.3)
        p.click()
        p.sleep(1)
        p.moveTo(367, 65, duration=0.3)
        p.click()
        p.sleep(1)
        p.typewrite('Hello, world!')
        p.PAUSE = 0.3
        p.press('Enter')
        return 
    return print("不匹配")

getSd(self=1)
matcha(self=1,bb="img\\bb.png",aa="img\\cc.png")