# -*- coding: utf-8 -*-

import logging.config
import os.path

def test():
    logging.error('123')

if __name__ == '__main__':
    #自定义变量 LOG_PATH
    dirname = os.path.dirname(__file__)
    logging.LOG_PATH = os.path.join(dirname, 'test.log')
    logging_file_path = os.path.join(dirname, 'logging.conf')
    logging.config.fileConfig('logging.conf')

    test()
