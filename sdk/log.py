# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
from functools import wraps
import logging


class Log(object):
    def __init__(self):
        # 创建 logger
        self.logger = logging.getLogger('Logger')
        self.logger.setLevel(logging.INFO)

        # 写入日志
        fh = logging.FileHandler('/Users/didi/Desktop/logs/runtime.log')
        fh.setLevel(logging.INFO)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # handler 输出格式
        formatter = logging.Formatter('[%(asctime)s][%(filename)s][%(levelname)s] ## %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 绑定 handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            self.logger.info("%s is excuted!" % func.__name__)
            return func(*args, **kwargs)
        return wrapped_function
