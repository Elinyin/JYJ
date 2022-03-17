#!/usr/bin/python
# coding:utf-8
"""
Create Time: 2022/3/14 16:38
Author: yinyilin
#!/usr/bin/env python
"""

import requests
class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()

    def visit(self,url,method, params=None,data=None,json=None, **kwargs):
        """
        访问一个接口，你可以使用get请求，也可以使用post请求，put，delete
        请求方法：mothod：
        请求地址：url
        请求参数：parsms，data,json
        :param url:
        :param method:
        :param params:
        :param data:
        :param json:
        :return:
        """
        # if method.lower() == "get":
        #     res = self.session.get(url,params=params,data=data,**kwargs)
        # elif method.lower() == "post":
        #     res = self.session.post(url,params=params,data=data,json=json,**kwargs)
        # else:
        # 可以处理请求方法
        res = self.session.request(method,url,params=params,data=data,json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")