#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/8 17:17
Author: yinyilin
"""

import unittest
from time import sleep
import os
from selenium import webdriver
from page.LoginPage import LoginPage
from ddt import ddt,file_data


@ddt
class Login_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.lg = LoginPage(cls.driver)
        os.path.abspath('.')

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()


    @file_data('../data/data.yaml')
    def test_case_001(self,**kwargs):
        self.lg.login_page(kwargs['username'], kwargs['password'])

    def test_case_002(self):
        self.lg.hover_()

    def test_case_003(self):
       self.lg.confirm_alert()

if __name__ == '__main__':
    unittest.main()