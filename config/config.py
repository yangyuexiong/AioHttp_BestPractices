# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 下午6:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : config.py
# @Software: PyCharm

import os
import configparser


def get_config():
    """获取配置文件"""
    conf = configparser.ConfigParser()
    AIO_SERVER_ENV = os.environ.get('AIO_SERVER_ENV')
    base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

    default_env = {
        'config_path': base_path + 'dev.ini',
        'msg': '本地配置文件:{}'.format(base_path + 'dev.ini'),
    }
    env_path_dict = {
        'default': default_env,
        'uat': {
            'config_path': base_path + 'uat.ini',
            'msg': 'uat配置文件:{}'.format(base_path + 'uat.ini'),
        },

        'production': {
            'config_path': base_path + 'prod.ini',
            'msg': 'prod配置文件:{}'.format('/srv/a/config/prod.ini')
        },
    }

    env_obj = env_path_dict.get(AIO_SERVER_ENV, default_env)
    msg = env_obj.get('msg')
    config_path = env_obj.get('config_path')
    print(config_path)
    print(msg)
    conf.read(config_path)

    # return conf

    conf_dict = {}
    for k, v in conf.items():
        conf_dict.update({k: {k: v for k, v in v.items()}})
    return conf_dict


if __name__ == '__main__':
    # conf_dict = {}
    # for k, v in conf.items():
    #     conf_dict.update({k: {k: v for k, v in v.items()}})
    print(get_config())
