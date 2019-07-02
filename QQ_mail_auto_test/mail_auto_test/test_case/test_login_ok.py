import sys
from selenium import webdriver
# 从其他包导入模块时，目标包相对当前目录路径有几层，需要在导入的包前面加几个“.”，表示层级关系
sys.path.append("./page_obj")
from .page_obj.page_login import *


driver = webdriver.Firefox()
pl = PageLogin(driver)

