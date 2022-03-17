#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/2/10 18:57
Author: yinyilin
"""
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# 基类
class Base:

    #构造函数
    def __init__(self,driver):
        self.driver = driver

    # 打开页面
    def open(self):
        self.driver.get(self.url)

    #隐式等待
    def implicitly(self):
        self.driver.implicitly_wait(5)

    #元素定位
    def element_loc(self,*loc):

        try:
            return WebDriverWait(self.driver,50).until(EC.presence_of_element_located(*loc))

        except TimeoutException as e:
            print('登录超时',e)
        except Exception as e:
            print('元素未定位到',e)

    #是否可点击
    def isclickable(self,loc):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc))
            return True
        except:
            return False

    #输入内容
    def send_key(self,loc,text):
        self.element_loc(loc).send_keys(text)

    #点击
    def click(self,loc):
        self.element_loc(loc).click()

    #切换 frame
    def change_frame(self,loc):
        frame = self.element_loc(loc)
        self.driver.switch_to.frame(frame)

    #释放 frame
    def default_frame(self):
        self.driver.switch_to_default_content()

    #弹框操作
    # def change_alert(self):
    #     a = self.webdriverwait(driver).until(EC.alert_is_present())
    #     return a

    # 切换alert
    def change_alert(self):
        self.driver.switch_to.alert()
    # 切换alert，点击确定按钮
    def alert_confirm(self):
        self.driver.switch_to_alert().accept()
    # 切换alert，点击取消按钮
    def alert_cancel(self):
        self.driver.switch_to_alert().dismiss()
    # 切换alert，发送文案
    def alert_sendkey(self,txt):
        self.driver.switch_to_alert().send_keys(txt)

    #鼠标悬停
    def hover(self,loc):
        sleep(3)
        ActionChains(self.driver).move_to_element(self.element_loc(loc)).perform()

    #退出浏览器
    def quit(self):
        self.driver.quit()