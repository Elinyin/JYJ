#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/8 15:13
Author: yinyilin
"""

from config.Base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class LoginPage(Base):

    url = 'https://crm.jinyingjie.com/index.php?m=user&a=login'
    user = (By.NAME, "name")
    pwd = (By.NAME, "password")
    but = (By.XPATH, '//*[@id="cont_enter_btn"]')

    me = (By.XPATH, '//*[@id="CRM_app"]/div/div[1]/ul/li/a')

    thread_tal = (By.XPATH,'//*[@id="CRM_app_menu_left"]/li[2]/a')
    thread = (By.XPATH,'//*[@id="CRM_app_slid"]/li[5]/a')

    detection_but = (By.XPATH,'//*[@id="checkUserBtn"]')

    iframe_ = (By.TAG_NAME,'iframe')


    def login_page(self,username,password):

        self.open()
        self.send_key(self.user,username)
        self.send_key(self.pwd,password)
        self.click(self.but)

    def hover_(self):
        self.hover(self.me)
        sleep(3)

    def confirm_alert(self):
        self.click(self.thread_tal)
        sleep(5)
        self.click(self.thread)
        sleep(3)
        self.change_frame(self.iframe_)
        sleep(3)
        self.click(self.detection_but)
        sleep(2)
        self.alert_confirm()
        self.default_frame()