# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午6:18
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : index.py
# @Software: PyCharm

from app.all_reference import *


class Index(web.View):

    async def get(self):
        # print(1 / 0)  # 测试异常
        # ab_code(666)  # 测试自定义异常
        return api_result(code=200, message='index api')
