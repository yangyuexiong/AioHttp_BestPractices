# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 上午10:10
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : login.py
# @Software: PyCharm


from app.all_reference import *


class LoginApi(web.View):

    async def get(self):
        sql = "select * from test;"
        db = MyAioMySQL(pool=self.request.app['aio_mysql_engine'])
        r = await db.query(sql)
        data = {
            "db_id": id(db),
            "r": r
        }
        return api_result(code=200, message='GET LoginApi', data=data)

    async def post(self):
        pool = self.request.app['aio_mysql_engine']
        db = MyAioMySQL(pool=pool)

        req_json_data = await self.request.json()
        username = req_json_data.get('username')
        password = req_json_data.get('password')

        sql = "select * from test where name='{}';".format(username)
        print(sql)

        user = await db.query(sql=sql, only=True)
        print(user)
        if user and user.get('pwd') == '123456':
            data = {
                "username": username,
                "password": password,
                "db id": id(db)
            }
            return api_result(code=200, message='POST LoginApi', data=data)
        else:
            ab_code(401)
