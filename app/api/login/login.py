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
        pool = self.request.app['aio_mysql_engine']
        db = MyAioMySQL(pool=pool)
        sql = "select * from test;"

        r = await db.query(sql=sql)
        print(r)
        r = await db.query(sql=sql, size=1)
        print(r)
        r = await db.query(sql=sql, only=True)
        print(r)

        sql = """INSERT INTO `AioHttp_BestPractices`.`test` (`name`) VALUES ('yyx3');"""
        await db.execute(sql=sql)

        pool = self.request.app['aio_redis_engine']
        r = MyAioRedis(pool=pool)
        print(await r.cache_set('test', '123456'))
        print(await r.cache_get('test'))
        print(await r.cache_del('test'))

        req_json_data = await self.request.json()
        username = req_json_data.get('username')
        password = req_json_data.get('password')
        data = {
            "username": username,
            "password": password,
        }

        return api_result(code=200, message='POST LoginApi', data=data)
