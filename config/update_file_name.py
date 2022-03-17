#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/13 16:02
Author: yinyilin
"""
import os

class Update_file_name:


    def update_file_name(self,path,new_name):
        # 读取地址中的文件列表
        fileList = os.listdir(path)

        n = 0
        for i in fileList:
            # 设置旧文件名（就是路径+文件名）
            oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符

            # 设置新文件名
            newname = path + os.sep + new_name

            os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名

            n += 1
