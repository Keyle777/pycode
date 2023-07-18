from wxauto import *


# 获取当前微信客户端
wx = WeChat()


# 获取会话列表
wx.GetSessionList()


# 输出当前聊天窗口聊天消息
msgs = wx.GetAllMessage
for msg in msgs:
    print('%s : %s'%(msg[0], msg[1]))
## 获取更多聊天记录
wx.LoadMoreMessage()
msgs = wx.GetAllMessage
for msg in msgs:
    print('%s : %s'%(msg[0], msg[1]))


# 向某人发送消息（以`文件传输助手`为例）
msg = '你好~'
who = '潘明超'
wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
wx.SendMsg(msg)  # 向`文件传输助手`发送消息：你好~


while True:
    # 向某人发送消息（以`文件传输助手`为例）
    msg = '你好~'
    who = '文件传输助手'
    wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    wx.SendMsg(msg)  # 向`文件传输助手`发送消息：你好~

## 发送换行消息（最近很多人问换行消息如何发送，新增说明一下）
msg = '''你好
这是第二行
这是第三行
这是第四行'''
who = '文件传输助手'
WxUtils.SetClipboard(msg)    # 将内容复制到剪贴板，类似于Ctrl + C
wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
wx.SendClipboard()   # 发送剪贴板的内容，类似于Ctrl + V
