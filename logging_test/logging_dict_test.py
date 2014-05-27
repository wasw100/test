# -*- coding: utf-8 -*-

import logging, logging.config
import logging_conf

logging.config.dictConfig(logging_conf.LOGGING_SETTING)

logger = logging.getLogger('test1')

logger.debug('debug')
logger.info('info')
logger.warn('warn')
logger.error('error')