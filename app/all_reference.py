# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 下午2:54
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : all_reference.py
# @Software: PyCharm

import json

from aiohttp import web

from common.libs.tools import json_format, MyAioMySQL, MyAioRedis
from common.libs.api_result import api_result
from registry.hook_register import ab_code
