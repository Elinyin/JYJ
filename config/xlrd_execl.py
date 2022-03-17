#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/11 17:54
Author: yinyilin
"""

import xlrd
import os

class ex():

    def e(self):

        os.path.abspath('.')
        # 打开文件 并读取
        data = xlrd.open_workbook('../data/data.xlsx','r')
        # 打开第一个sheet
        table = data.sheet_by_index(0)
        # 获取第一列
        keys = table.row_values(0)
        # 获取行数
        nrows = table.nrows
        #获取列数
        ncols = table.ncols

        if nrows <= 1:
            print('总数小于1')

        else:
            r = []
            j = 1
            for i in range(nrows-1):
                s = {}
                values = table.row_values(j)
                for x in range(ncols):
                    s[keys[x]] = values[x]
                r.append(s)
                j+=1
        return r

if __name__ == '__main__':
    l = ex.e('')


