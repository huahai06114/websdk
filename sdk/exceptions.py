# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
import json


class APIException(Exception):
    code = 500
    msg = '抱歉，服务器未知错误'
    data = ''

    def __init__(self, msg=None, code=None, data=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if data:
            self.data = data

    def __str__(self):
        body = dict(
            msg=self.msg,
            data=self.data,
            code=self.code
        )
        text = json.dumps(body)
        return text


class Success(APIException):
    code = 0
    msg = 'success'
    data = ''


class Failed(APIException):
    code = 1
    msg = 'failed'
    data = ''


class NotFound(APIException):
    code = 404
    msg = '资源不存在'
    data = ''


class NotPermission(APIException):
    code = 403
    msg = '没有权限'
    data = ''


class ParameterException(APIException):
    code = 400
    msg = 'parameter error'
    data = ''


class UnknownException(APIException):
    code = 500
    msg = '服务器未知错误'
    data = ''


class Forbidden(APIException):
    code = 401
    msg = '不可操作'
    data = ''


class RepeatException(APIException):
    code = 400
    msg = '字段重复'
    data = ''
