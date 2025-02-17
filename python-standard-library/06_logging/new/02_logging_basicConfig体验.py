#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import logging

# 基础配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='example.log',
    filemode='w',
    errors='replace',
    encoding="utf-8")

# 记录不同级别的日志
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
