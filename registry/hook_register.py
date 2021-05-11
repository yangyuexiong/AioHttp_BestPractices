# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午10:13
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : hook_register.py
# @Software: PyCharm

import re
import json

from aiohttp import web

from common.libs.tools import json_format

custom_resp_dict = {
    333: '测试自定义异常',
    400: '参数类型错误',
    401: '未登录_认证信息失败_令牌过期',
    403: '无权限',
    500: '服务器异常',
    666: 'Token?',
    777: 'Sql注入警告',
    996: '没救了'
}


class CustomException(BaseException):

    def __init__(self, code, message):
        self.code = code
        self.message = message


def ab_code(data):
    C = custom_resp_dict
    code = data
    message = C.get(data, 'ERROR')
    raise CustomException(code=code, message=message)


@web.middleware
async def before_middleware(request, handler):
    method = request.method
    url = request.url
    path = request.path
    headers = request.headers
    has_body = request.has_body
    req_json = request.json
    print(method)
    print(url)
    print(path)
    print('=== request headers ===')
    json_format({k: v for k, v in headers.items()})

    if has_body:
        print('=== request json data ===')
        req_json = await req_json()
        for val in req_json.values():
            val = str(val).lower()
            pattern = r"\b(and|like|exec|insert|select|drop|grant|alter|delete|update|count|chr|mid|master|truncate|char|delclare|or)\b|(\*|;)"
            r = re.search(pattern, val)
            if r:
                print(val)
                resp = {
                    "code": 777,
                    "message": "CustomException:【Sql注入警告】",
                    "data": "{} {}".format(method, path)
                }
                json_format(resp)
                return web.json_response(resp)
            else:
                pass

        json_format(req_json)
    else:
        json_format({})

    # w = ['/api', '/api/login']
    # if path in w:
    #     # print(request.headers.get('token'))
    #     response = await handler(request)
    #     print('=== response ===')
    #     json_format(json.loads(bytes.decode(response.body)))
    #     return response
    # else:
    #     resp = {
    #         "code": 666,
    #         "message": "CustomException:【Token?】",
    #         "data": "{} {}".format(method, path)
    #     }
    #     json_format(resp)
    #     return web.json_response(resp)

    response = await handler(request)
    print('=== response ===')
    json_format(json.loads(bytes.decode(response.body)))
    return response


@web.middleware
async def error_middleware(request, handler):
    method = request.method
    path = request.path
    resp = {
        "code": "",
        "message": "",
        "data": "{} {}".format(method, path),
    }
    try:
        response = await handler(request)
        return response

    except BaseException as e:

        if isinstance(e, web.HTTPException):
            print('=== HTTPException ===')
            resp['code'] = e.status
            resp['message'] = "HTTPException:【{}】".format(bytes.decode(e.body))
            print(resp)
            return web.json_response(resp)

        elif isinstance(e, Exception):
            print('=== Exception ===')
            resp['code'] = 500
            resp['message'] = "Exception:【{}】".format(e)
            print(resp)
            return web.json_response(resp)

        elif isinstance(e, CustomException):
            print('=== CustomException ===')
            resp['code'] = e.code
            resp['message'] = "CustomException:【{}】".format(e.message)
            print(resp)
            return web.json_response(resp)


@web.middleware
async def middleware1(request, handler):
    print('Middleware 1 called')
    response = await handler(request)
    print('Middleware 1 finished')
    return response


@web.middleware
async def middleware2(request, handler):
    print('Middleware 2 called')
    response = await handler(request)
    print('Middleware 2 finished')
    return response


def register_hook(app):
    """中间件注册"""

    app.middlewares.append(before_middleware)
    app.middlewares.append(error_middleware)
    app.middlewares.append(middleware1)
    app.middlewares.append(middleware2)
