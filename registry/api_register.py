# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午6:21
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : api_register.py
# @Software: PyCharm

from app.api import *


def register_api(app):
    """Api注册"""

    app.router.add_route('*', '/api', Index)
    app.router.add_route('*', '/api/login', LoginApi)
    app.router.add_route('*', '/api/test', TestApi)
