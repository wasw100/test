#! -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

def show_log():
    logger.error('operate __name__ is %s' % __name__)
    logger.debug('operate debug')
    logger.info('operate info')
    logger.warn('operate warn')
    logger.error('operate error')