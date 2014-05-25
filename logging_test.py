# -*- coding: utf-8 -*-
"""
https://docs.python.org/2/howto/logging-cookbook.html
"""

import logging

# create logger with 'spam_application'
logger2 = logging.getLogger('logging_test.log2')
logger = logging.getLogger('logging_test')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

#if no this line, StreamHandler is invalid
logging.basicConfig(level=logging.ERROR)

logger.info('creating an instance of auxiliary_module.Auxiliary')
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
logger.info('done with auxiliary_module.some_function()')
logger2.info('logger2 info')