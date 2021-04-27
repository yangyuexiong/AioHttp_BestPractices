# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午6:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm

import argparse

from aiohttp import web

from ApplicationExample import create_app

app = create_app()


def main():
    parser = argparse.ArgumentParser(description="Aio Server")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='this is a host')
    parser.add_argument('--port', type=int, default='9099', help='this is a port')
    args = parser.parse_args()
    host = args.host
    port = args.port
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
