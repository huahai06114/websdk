# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
import logging
import os

log_fmt = ' | '.join(('%(asctime)s', '%(levelname)s', '%(message)s'))
log_key = 'logger_key'


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Logger(object):
    def __init__(self, log_file='/tmp/xxx.log'):
        self.__log_key = log_key
        self.log_file = log_file

    def term_log(self, log_level, log_message):
        # 创建一个logger
        logger = logging.getLogger(self.__log_key)
        logger.setLevel(logging.DEBUG)

        # 创建一个handler用于输出到终端
        th = logging.StreamHandler()
        th.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(log_fmt)
        th.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(th)

        ###记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}
        level_dic[log_level](log_message)

        th.flush()
        logger.removeHandler(th)

    def file_log(self, log_level, log_message):
        # 创建一个logger
        logger = logging.getLogger(self.__log_key)
        logger.setLevel(logging.DEBUG)

        # 建立日志目录
        log_dir = os.path.dirname(self.log_file)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        # 创建一个handler用于写入日志文件
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(log_fmt)
        fh.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)

        # 记录日志
        level_dic = {'debug': logger.debug, 'info': logger.info, 'warning': logger.warning, 'error': logger.error,
                     'critical': logger.critical}
        level_dic[log_level](log_message)

        # 删除重复记录
        fh.flush()
        logger.removeHandler(fh)


# 初始化是可以指定日志文件的存储目录
Log = Logger()
Log.term_log('info', 'xxxx')
Log.file_log('info', 'xxxx')
