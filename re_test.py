# -*- coding: utf-8 -*-

import re

def test():
    s = 'a123b'
    m = re.search(r'\d+', s)
    if m:
        print m.group()
    else:
        print 'no match'

if __name__ == '__main__':
    test()
