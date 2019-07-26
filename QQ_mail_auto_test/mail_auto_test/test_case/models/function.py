import os
import time
import win32gui
import win32api
import win32con
import pyautogui
from ctypes import *
from selenium.webdriver import ActionChains


def qq_login():
    # TODO: 可以将密码账户作为参数传入
    # 运行QQ
    os.system('"C:\Program Files (x86)\Tencent\QQLite\Bin\QQScLauncher.exe"')
    time.sleep(5)
    a = win32gui.FindWindow(None, "QQ")  # 获取窗口的句柄，参数1: 类名，参数2： 标题QQ
    login_id = win32gui.GetWindowPlacement(a)
    windll.user32.SetCursorPos(login_id[4][0]+300, login_id[4][1]+273)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 按下鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 放开鼠标
    time.sleep(0.2)
    # 输入账号
    # pyautogui.typewrite(["1", "4", "1", "4", "7", "1", "0", "8", "2", "3"])
    pyautogui.typewrite("1414710823")
    time.sleep(1)

    # tab切换
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    # pyautogui.typewrite(["L", "J", "H", "-", "l", "j", "h", "@", "1", "6", "9", "9", "1", "4", "@"])
    pyautogui.typewrite("LJH-ljh@169914@")
    time.sleep(1)

    # 点击回车键登录
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)


def open_mail_web():
    os.system(r'"D:\Program Files\Mozilla Firefox\firefox.exe"')
    time.sleep(2)

    pyautogui.click(305, 53)  # 移动鼠标到URL输入栏，并点击获取焦点
    pyautogui.press('backspace')  # 删除之前的URL
    pyautogui.typewrite('https://mail.qq.com/')  # 输入QQ邮箱地址
    # 按enter进入网页
    for i in range(2):
        pyautogui.press('enter')
    time.sleep(2)
    pyautogui.screenshot("./mail_auto_test/report/img/unable_auto_login.jpg")  # 截图证明不能自动登录
    pyautogui.click(1893, 11)  # 关闭当前网页


def get_screenshot(driver, filename):
    driver.get_screenshot_as_file(filename)


def mouseover(driver, *loc):
    above = driver.find_element(*loc)
    ActionChains(driver).move_to_element(above).perform()
    time.sleep(2)



