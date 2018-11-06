# -*- coding: utf-8 -*-
""" 
@author:wangcheng 
@file: log.py 
@time: 2018/10/25 
"""

import logging
import logging.config
from logging.handlers import RotatingFileHandler
from os.path import join,dirname,abspath

base_path=dirname(dirname(abspath(__file__)))
# print(path)
current_path=join(base_path,'var','log')
# print(current_path)
log_format='%(asctime)s %(name)s[line:%(lineno)d] %(levelname)-s %(message)s'


def get_logger(file_path=None):
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        if file_path:
            log_path=join(current_path,file_path)
        else:
            # 日志输出到文件
            log_path=join(current_path,'log.log')
        fh=RotatingFileHandler(filename=log_path,maxBytes=50*1024*1024,backupCount=40)
        formatter=logging.Formatter(log_format)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        # 日志输出到console
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.setLevel(logging.DEBUG)
    return logger
