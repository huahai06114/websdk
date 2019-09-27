# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：常量管理
"""


class ConstError(TypeError):
    pass


class _const(object):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ConstError("can't rebind const (%s)" % name)
        if not name.isupper():
            raise ConstError("Const must be upper.")
        self.__dict__[name] = value


const = _const()

# MySQL 配置相关
const.DB_CONFIG_ITEM = 'databases'
const.DBHOST_KEY = 'host'
const.DBPWD_KEY = 'pwd'
const.DBUSER_KEY = 'user'
const.DBNAME_KEY = 'name'
const.DBPORT_KEY = 'port'
const.SF_DB_KEY = 'vmobel'
const.DEFAULT_DB_KEY = 'default'

# redis 配置相关
const.REDIS_CONFIG_ITEM = 'redises'
const.RD_HOST_KEY = 'host'
const.RD_PORT_KEY = 'port'
const.RD_DB_KEY = 'db'
const.RD_AUTH_KEY = 'auth'
const.RD_CHARSET_KEY = 'charset'
const.RD_DECODE_RESPONSES = 'decode_responses'
const.RD_PASSWORD_KEY = 'password'
const.DEFAULT_RD_KEY = 'default'

# app settings
const.APP_SETTINGS = 'APP_SETTINGS'

# all user info
const.USERS_INFO = 'USERS_INFO'

# e-mail
const.EMAIL_SUBJECT_PREFIX = "EMAIL_SUBJECT_PREFIX"
const.EMAIL_HOST = "EMAIL_HOST"
const.EMAIL_PORT = "EMAIL_PORT"
const.EMAIL_HOST_USER = "EMAIL_HOST_USER"
const.EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD"
const.EMAIL_USE_SSL = "EMAIL_USE_SSL"
const.EMAIL_USE_TLS = "EMAIL_USE_TLS"

