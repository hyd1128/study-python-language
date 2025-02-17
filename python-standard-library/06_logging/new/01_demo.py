#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import logging

# 基础配置
logging.basicConfig(filename='example.log', encoding="utf-8", level=logging.DEBUG)

# 记录不同级别的日志
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like 123resund and Malmö')

