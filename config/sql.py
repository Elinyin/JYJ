#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/11 17:57
Author: yinyilin
"""

import pymysql as mysql

class MYSQL():

    host= ''
    user = ''
    pwd = ''

    #连接数据库
    conn = mysql.connect(host=host,user=user,password=pwd,db='mysql',charset='utf-8')
    # 获取游标
    cursor = conn.cursor()
    # 执行 sql 语句
    cursor.execute('select * from jyj_crm')
    # 获取全部值
    cursor.fetchall()