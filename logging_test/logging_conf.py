# -*- coding: utf-8 -*-

import os.path

LOGGING_SETTING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format':'%(asctime)s %(levelname)-6s %(name)-10s %(message)s',
            'datefmt':'%Y-%m-%d %H:%M:%S',
        },
        'tornado': {
            'format': '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
            'datefmt': '%y%m%d %H:%M:%S',
        }
    },
    'handlers': {
        'default': {
            'class':'logging.StreamHandler',
            'formatter':'tornado',
        },
        'file': {
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter':'tornado',
            'filename':os.path.join(os.path.dirname(__file__), 'test.log'),
            'when':'midnight',
            'interval':1,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'test1': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}