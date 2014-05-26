# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('operate.haha.test2')

def show_log2():
    logger.error('test2 logger name, %s' % logger.name)
    logger.debug('test2 debug')
    logger.info('test2 info')
    logger.warn('test2 info')
    logger.error('test2 error')