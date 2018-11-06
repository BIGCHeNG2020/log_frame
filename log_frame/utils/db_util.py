# -*- coding: utf-8 -*-
""" 
@author:wangcheng 
@file: db_util.py 
@time: 2018/10/25 
"""


import logging
from utils.log import get_logger

logger=get_logger()

def connect():
    logger.info('this is db_util')
    logger.error('this is db_util error')