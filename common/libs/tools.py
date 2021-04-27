# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 下午5:20
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tools.py
# @Software: PyCharm

import json


def json_format(d):
    try:
        print(json.dumps(
            d,
            sort_keys=True,
            indent=4,
            separators=(', ', ': '),
            ensure_ascii=False
        ))
    except BaseException as e:
        print(d)
