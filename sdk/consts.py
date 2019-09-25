# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：常量管理
"""
from enum import IntEnum as Enum


class IntEnum(Enum):
    @classmethod
    def find_enum(cls, value):
        for k, v in cls._value2member_map_.items():
            if k == value:
                return v
        return None


class ErrorCode():
    """ 错误码枚举 """

    not_found = 404
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_allowed = 405
    not_acceptable = 406
    conflict = 409
    gone = 410
    precondition_failed = 412
    request_entity_too_large = 413
    unsupport_media_type = 415
    internal_server_error = 500
    service_unavailable = 503
    service_not_implemented = 501
    handler_uncatched_exception = 504
    config_import_error = 1001
    config_item_notfound_error = 1002


class ConstError(TypeError):
    pass


class _const(object):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ConstError("can't rebind const (%s)" % name)
        if not name.isupper():
            raise ConstError("Const must be upper.")
        self.__dict__[name] == value


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
const.READONLY_DB_KEY = 'readonly'

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

# MQ 配置相关
const.MQ_CONFIG_ITEM = 'mqs'
const.MQ_ADDR = 'MQ_ADDR'
const.MQ_PORT = 'MQ_PORT'
const.MQ_VHOST = 'MQ_VHOST'
const.MQ_USER = 'MQ_USER'
const.MQ_PWD = 'MQ_PWD'
const.DEFAULT_MQ_KEY = 'default'

