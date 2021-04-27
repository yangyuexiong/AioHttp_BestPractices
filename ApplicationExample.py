# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午9:09
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : ApplicationExample.py
# @Software: PyCharm


from aiohttp import web

from registry.api_register import register_api
from registry.conf_register import register_conf
from registry.hook_register import register_hook


async def create_app():
    """应用实例"""
    app = web.Application()
    register_api(app)  # 路由注册
    register_conf(app)  # 配置文件注册
    register_hook(app)  # 中间件注册
    return app
