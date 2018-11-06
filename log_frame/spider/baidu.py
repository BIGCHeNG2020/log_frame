# -*- coding: utf-8 -*-
""" 
@author:wangcheng 
@file: baidu.py 
@time: 2018/10/25 
"""

import requests
from utils.log import get_logger
from utils.db_util import connect

logger=get_logger()

def run():
    url='http_methods://www.baidu.com'
    ret=requests.get(url)
    print(ret.status_code)
    logger.info('this is baidu')
    logger.error('this is baidu error')
    connect()


if __name__ == '__main__':
    run()
