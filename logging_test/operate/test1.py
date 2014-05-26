# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

def show_log1():
    print 1
    logger.error('test1 logger name, %s' % logger.name)
    logger.debug('test1 debug')
    logger.info('test1 info')
    logger.warn('test1 warn')
    logger.error('test1 error')