# -*- coding: utf-8 -*-

import re

def test():
    s = 'a123b456c'
    m = re.search(r'\d+', s)
    if m:
        print m.group()
    else:
        print 'no match'

    ds = re.findall(r'\d+', s)
    print ds

if __name__ == '__main__':
    test()
