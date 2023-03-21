import ctypes
import time
from win32gui import GetCursorPos
import pyautogui

try:
    gm = ctypes.CDLL(r'./ghub_device.dll')#DLL要放在py文件同级目录下
    gmok = gm.device_open() == 1
    if not gmok:
        print('未安装ghub或者lgs驱动!!!')
    else:
        print('初始化成功!')
except FileNotFoundError:
    print('缺少ghub_device文件')

#按下鼠标按键
def press_mouse_button(button):
    if gmok:
        gm.mouse_down(button)   #code: 1:左键, 2:中键, 3:右键, 4:侧下键, 5:侧上键, 6:DPI键

#松开鼠标按键
def release_mouse_button(button):
    if gmok:
        gm.mouse_up(button)     #code: 1:左键, 2:中键, 3:右键, 4:侧下键, 5:侧上键, 6:DPI键

#点击鼠标
def click_mouse_button(button):
    press_mouse_button(button)
    release_mouse_button(button)

#按下键盘按键
def press_key(code):
    if gmok:
        gm.key_down(code)#键盘按键函数中，传入的参数采用的是键盘按键对应的键码 code: 'a'-'z':A键-Z键, '0'-'9':0-9, 其他的没猜出来

#松开键盘按键
def release_key(code):
    if gmok:
        gm.key_up(code)

#点击键盘按键
def click_key(code):#里面的code改为'w'，一定要小写，命令书写 click_key('w') 实现点击w键功能
    press_key(code)
    release_key(code)

# 鼠标移动  罗技的函数直接使用只能相对移动  注意关闭系统和驱动两个地方的加速
def move(x, y, absolute=False):#move(10, 10, absolute=True) True是移动到x，y位置 False是基于目前位置再移动参数
    if gmok:
        if x == 0 and y == 0:
            return
        mx, my = x, y
        if absolute:
            ox, oy = GetCursorPos()#获取当前光标位置
            mx = x - ox
            my = y - oy
        gm.moveR(mx, my, True)





if __name__=='__main__':
    #要求打开鼠标软件，以管理员运行py文件
    #鼠标绝对移动
    for i in range(300):
        time.sleep(0.01)
        move(i, i, absolute=True)

    #鼠标相对移动
    time.sleep(0.01)
    move(300, 300, absolute=False)

    #鼠标点击
    click_mouse_button(2)

    #按键点击
    time.sleep(0.1)
    click_key("w")

    print("调试结束")