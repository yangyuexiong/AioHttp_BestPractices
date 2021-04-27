# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 上午10:10
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : login.py
# @Software: PyCharm


from app.all_reference import *


class LoginApi(web.View):

    async def get(self):
        return api_result(code=200, message='GET LoginApi', data=[{}])

    async def post(self):
        req_json_data = await self.request.json()
        username = req_json_data.get('username')
        password = req_json_data.get('password')
        data = {
            "username": username,
            "password": password,
        }
        return api_result(code=200, message='POST LoginApi', data=data)
