# -*- coding: utf-8 -*-

import re

def test():
    s = 'a123b456c'
    m = re.search(r'\d+', s)
    if m:
        print 'm', m.group()
    else:
        print 'm is None'

    ds = re.findall(r'\d+', s)
    print 'ds', ds

    m2 = re.match(r'\d+', s)
    print 'm2', m2

    #从开头开始匹配
    m3 = re.match(r'.+', s)
    if m3:
        print 'm3', m3.group()
    else:
        print 'm3 is None'

    m4 = re.match(r'.+?', s)
    if m4:
        print 'm4', m4.group()
    else:
        print 'm4 is None'


def test2():
    pattern = re.compile(r'hello')
    match = pattern.match('hello world!')
    if match:
        print match.group()

if __name__ == '__main__':
    test()
