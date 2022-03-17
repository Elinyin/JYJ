#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/13 16:02
Author: yinyilin
"""

import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner

#测试用例目录
test_dir = os.path.dirname(os.path.abspath(__file__))

# 测试报告路径
report_path = os.path.join((test_dir),"report")

# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#
# #html报告文件路径
# report_abspath = os.path.join(report_path, "result_"+now+".html")

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*_case.py")


if __name__ == '__main__':

    # with open(report_path,"wb") as report:

    runner = HTMLTestRunner(title=r'接口自动化测试报告,测试结果如下：',description=r'用例执行情况：')

    runner.run(discover)

