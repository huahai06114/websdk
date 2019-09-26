# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
from enum import IntEnum as Enum


class IntEnum(Enum):
    @classmethod
    def find_enum(cls, value):
        for k, v in cls._value2member_map_.items():
            if k == value:
                return v
        return None


class ErrorCode(IntEnum):
    """ 错误码枚举 """

    success_request = 0
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_found = 404
    not_allowed = 405
    not_acceptable = 406
    conflict = 409
    parameter_error = 410
    precondition_failed = 412
    request_entity_too_large = 413
    unsupport_media_type = 415
    internal_server_error = 500
    service_unavailable = 503
    service_not_implemented = 501
    handler_uncatched_exception = 504
    config_import_error = 1001
    config_item_notfound_error = 1002


class BaseError(Exception):
    """ 错误基类，所有的错误必须从该继承 """

    def __init__(self, error_code, *args, **kwargs):
        if isinstance(error_code, IntEnum):
            self._error_code = error_code
            self.kwargs = kwargs

            super(BaseError, self).__init__(*args)
        else:
            raise TypeError('Error code must be ErrorCode type.')

    @property
    def error_code(self):
        return self._error_code


class Success(BaseError):
    """ 成功类 """
    def __init__(self, *args, **kwargs):
        super(Success, self).__init__(ErrorCode.success_request, *args, **kwargs)


class BadRequestError(BaseError):
    """ 错误的请求 """

    def __init__(self, *args, **kwargs):
        super(BadRequestError, self).__init__(ErrorCode.bad_request, *args, **kwargs)


class NotFoundError(BaseError):
    """ 资源不存在 """

    def __init__(self, *args, **kwargs):
        super(NotFoundError, self).__init__(ErrorCode.not_found, *args, **kwargs)


class UnknownError(BaseError):
    """ 服务器未知错误 """

    def __init__(self, *args, **kwargs):
        super(UnknownError, self).__init__(ErrorCode.internal_server_error, *args, **kwargs)


class ForbiddenError(BaseError):
    """ 禁止操作 """

    def __init__(self, *args, **kwargs):
        super(ForbiddenError, self).__init__(ErrorCode.forbidden, *args, **kwargs)


class ParameterError(BaseError):
    """ 禁止操作 """

    def __init__(self, *args, **kwargs):
        super(ParameterError, self).__init__(ErrorCode.parameter_error, *args, **kwargs)


class ConfigError(Exception):
    def __init__(self, config_key, *args, **kwargs):
        self.config_key = config_key
        super(ConfigError, self).__init__(*args, **kwargs)
