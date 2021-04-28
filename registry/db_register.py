# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午8:36
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : db_register.py
# @Software: PyCharm


import asyncio
import aiomysql
import aioredis

from config.config import get_config

conf = get_config()


async def register_db(app):
    """
    aio mysql pool注册
    :param app:
    :return:
    """
    aio_mysql_conf = app.get('config').get('mysql')
    aio_mysql_conf['port'] = int(aio_mysql_conf.get('port'))
    app['aio_mysql_engine'] = await aiomysql.create_pool(**aio_mysql_conf, charset='utf8', loop=app.loop)
    yield
    app['aio_mysql_engine'].close()
    await app['aio_mysql_engine'].wait_closed()


async def register_redis(app):
    """
    aio redis pool注册
    :param app:
    :return:
    """
    aio_redis_conf = app.get('config').get('redis')
    address = (aio_redis_conf.get('redis_host'), aio_redis_conf.get('redis_port'))
    db = int(aio_redis_conf.get('redis_db'))
    password = aio_redis_conf.get('redis_pwd')
    app['aio_redis_engine'] = await aioredis.create_pool(address=address, db=db, password=password, loop=app.loop)
    yield
    app['aio_redis_engine'].close()
    await app['aio_redis_engine'].wait_closed()

if __name__ == '__main__':
    print(conf)