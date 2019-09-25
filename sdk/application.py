# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
from shortuuid import uuid
from tornado import httpserver, ioloop
from tornado import options as tnd_options
from tornado.options import options, define
from tornado.web import Application as tornadoApp

from .logger import Logger
from .configs import configs


define('addr', default='0.0.0.0', help="run on the given ip address", type=str)
define('port', default=8000, help="run on the given port", type=int)
define('progid', default=str(uuid()), help="tornado progress id", type=str)


# 启动项目时，需加上参数 --addr="xxx.xxx.xxx.xxx" --port=8989 --progid="1111"
class Application(tornadoApp):
    """
        定制 Tornado Application 集成日志、sqlalchemy 等功能
    """

    def __init__(self, **settings):
        tnd_options.parse_command_line()
        if configs.can_import:
            configs.import_dict(**settings)
        Logger.info('%s' % options.progid)
        super(Application, self).__init__(**settings)

        http_server = httpserver.HTTPServer(self)
        http_server.listen(options.port, address=options.addr)
        self.io_loop = ioloop.IOLoop.instance()

    def start_request(self):
        """
            启动 tornado 服务
        """
        try:
            Logger.info('progressid: %(progid)s' % dict(progid=options.progid))
            Logger.info('server address: %(addr)s:%(port)d' % dict(addr=options.addr, port=options.port))
            Logger.info('web server start sucessfuled.')
            self.io_loop.start()
        except KeyboardInterrupt:
            self.io_loop.stop()
        except:
            import traceback
            Logger.error('%(tra)s' % dict(tra=traceback.format_exc()))


if __name__ == '__main__':
    pass
