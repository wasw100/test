# -*- coding: utf-8 -*-
"""
https://docs.python.org/2/library/urlparse.html
"""

import urlparse

def test():
    o = urlparse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html?a=1&a=2&c=5')
    print o
    qs = o.query
    print urlparse.parse_qs(qs)
    print urlparse.parse_qsl(qs)


#TODO requests urllib list params handle

if __name__ == '__main__':
    test()
