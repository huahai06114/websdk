#### 一、结构
```shell
.
├── README.md    项目readme
└── sdk      web开发使用
    ├── __init__
    ├── application.py          tornado application
    ├── base_handler.py         tornado handler 基类
    ├── cache.py                redis 缓存
    ├── configs.py              配置文件管理
    ├── consts.py               常量
    ├── db_context.py           MySQL 处理类
    ├── exceptions.py           异常
    ├── auths.py                jwt 认证
    ├── mqhelper.py             MQ 处理类
    ├── program.py              Program 类
    ├── tools.py                工具类
    └── log.py                  日志处理
```

#### 2、安装方法
在已经安装 Python3 的环境中，可直接使用下面的命令进行安装：
```python
pip3 install -U git+https://github.com/KHdvip/websdk.git
```
安装完成后，就可以像引用其他三方模块一样使用了。
```python
from sdk import *
```