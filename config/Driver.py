#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/2/10 18:55
Author: yinyilin
"""
from appium.webdriver import webdriver


class Driver:

    def init_driver(self):

        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "8.0.0"  # 更换设备需要改 3-1
        desired_caps["deviceName"] = "FIG-TL00"  # 更换设备需要改 3-2
        desired_caps["appPackage"] = "com.jiaoyu.jinyingjie"
        desired_caps["appActivity"] = ".StartActivity"  # 更换设备需要改 3-3
        desired_caps["automationName"] = "UiAutomator1"
        #        desired_caps["unicodeKeyboard"] = True  # 使用Appium自带的输入法
        #        desired_caps["unicodeKyboard"] = True  # 使用Unicode输入法
        #        desired_caps["resetKeyboard"] = True  # 输入法复位

        command_execuator = "http://localhost:4723/wd/hub"

        driver = webdriver.Remote(command_execuator, desired_caps)

        return driver