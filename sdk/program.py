# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
import fire


class MainProgram(object):

    @staticmethod
    def run(cls_inst):
        if issubclass(cls_inst, MainProgram):
            fire.Fire(cls_inst)
        else:
            raise Exception('')
