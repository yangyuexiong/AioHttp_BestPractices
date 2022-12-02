# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 上午11:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test.py
# @Software: PyCharm

from app.all_reference import *


class TestApi(web.View):

    async def get(self):
        return api_result(code=200, message='GET TestApi', data=[{}])

    async def post(self):
        pool = self.request.app['aio_mysql_engine']
        db = MyAioMySQL(pool=pool)
        sql = "select * from test;"

        res1 = await db.pool_query(sql=sql)
        print(res1)
        res2 = await db.pool_query(sql=sql, size=1)
        print(res2)
        res3 = await db.pool_query(sql=sql, only=True)
        print(res3)

        sql = """INSERT INTO `AioHttp_BestPractices`.`test` (`name`) VALUES ('yyx3');"""
        await db.pool_execute(sql=sql)

        R = self.request.app['aio_redis_engine']
        r_set = await R.set('test', '123456')
        r_get = await R.get('test')
        r_delete = await R.delete('test')

        req_json_data = await self.request.json()
        username = req_json_data.get('username')
        password = req_json_data.get('password')
        data = {
            "username": username,
            "password": password,
            "pool_id": id(pool),
            "mysql_id": id(db),
            "mysql_query_id": id(db.pool_query),
            "redis_id": id(R),
            "redis_query_id": id(R.get),
            # "res1": res1,
            # "res2": res2,
            # "res3": res3,
            "r_set": r_set,
            "r_get": r_get,
            "r_delete": r_delete
        }

        return api_result(code=200, message='POST LoginApi', data=data)
