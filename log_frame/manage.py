# -*- coding: utf-8 -*-
""" 
@author:wangcheng 
@file: manage.py 
@time: 2018/10/26 
"""

import sys,os
from utils.log import get_logger

log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'var','log')

if __name__ =='__main__':
    try:
        spider_name=sys.argv[1]
    except:
        print('format: python3 manage.py baidu')
        sys.exit(-1)
    log_path=os.path.join(log_path,spider_name)
    if os.path.exists(log_path):
        os.remove(log_path)
        print('delete {} success'.format(log_path))
    logger = get_logger(file_path=log_path)
    logger.info('exe {}.py'.format(spider_name))
    from importlib import import_module
    module=import_module('spider.{}'.format(spider_name))
    module.run()
