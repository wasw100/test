#! -*- coding: utf-8 -*-
"""
logging config from file
"""

import logging
import logging.config
import operate
from operate import test1, test2

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

def main():
    logger.debug('main debug')
    logger.info('main info')
    logger.warn('main warn')
    logger.error('main error')
    operate.show_log()
    test1.show_log1()
    test2.show_log2()

if __name__ == '__main__':
    main()

