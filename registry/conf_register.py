# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午8:26
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : conf_register.py
# @Software: PyCharm

from config.config import get_config


def register_conf(app):
    """配置文件"""

    app['config'] = get_config()
