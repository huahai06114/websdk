# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
import sys
import traceback
import logging
import logging.config
import multiprocessing


class QueueLog(object):
    queue = None
    debug = False

    # 指定日志写入的 queue
    @classmethod
    def set_queue(cls, queue):
        cls.queue = queue

    # 日志写入queue
    @staticmethod
    def collect(msg):
        if Logger.debug:
            print(msg)
        Logger.queue.put(msg)

    @staticmethod
    def info_to_queue(*args, **kwargs):
        log_str = ' | '.join(['%s=%s' % (k, v) for k, v in kwargs.items()])
        log_str = log_str + ' | '.join(args)
        Logger.collect(('info', log_str))

    @staticmethod
    def error_to_queue(*args, **kwargs):
        log_str = ' | '.join(['%s=%s' % (k, v) for k, v in kwargs.items()])
        log_str = log_str + ' | '.join(args)
        Logger.collect(('error', log_str))


# 指定日志存储 queue
log_queue = multiprocessing.Queue()
QueueLog.set_queue(log_queue)
log = QueueLog()


class Logger(object):

    @staticmethod
    def info(key, msg='', kwargs=''):
        param = {}
        param['mark'] = key
        param['msg'] = msg
        param["param"] = str(kwargs)
        log.info(**param)

    @staticmethod
    def error(key, msg='', kwargs='', ex=None):
        param = {}
        param['mark'] = key
        param['msg'] = msg
        param["param"] = str(kwargs)
        if isinstance(ex, Exception):
            exc_type, exc_value, exc_traceback_obj = sys.exc_info()
            traceback.print_tb(exc_traceback_obj)
            param['ex-sim'] = str(ex)
            param['ex'] = traceback.format_exc()
        log.error(**param)


# 将队列中的日志信息写入文件
def log_save_to_file():
    logging.config.fileConfig('app/common/log.conf')
    info_log = logging.getLogger('mark_logger')
    error_log = logging.getLogger('root_logger')

    print("log process start.......")
    while True:
        log_type, msg_str = log_queue.get()
        if log_type == 'info':
            info_log.info(msg_str)
        elif log_type == 'error':
            error_log.error(msg_str)


# 日志写入文件进程
def log_save_process():
    log_process = multiprocessing.Process(target=log_save_to_file, name="log")
    log_process.start()
