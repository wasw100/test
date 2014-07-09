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
    """完全匹配"""
    m1 = re.match(r'\d+$', '123')
    if m1:
        print 'm1', m1.group()
    else:
        print 'm1 is None'

    m2 = re.search(r'^\d+$', '123')
    if m2:
        print 'm2', m2.group()
    else:
        print 'm2 is None'


def test3():
    pattern = re.compile(r'hello')
    match = pattern.match('hello world!')
    if match:
        print match.group()

def find_all_test():
    s = 'a123b456c'
    ds = re.findall('\d+?', s)
    print ds
    ds2 = re.findall('\d+', s)
    print ds2


def find_all_test2():
    s = 'a123b456c'
    ds = re.finditer('\d+', s)
    print ds
    for m in ds:
        print m.group()


def re_sub_test():
    def replace(m):
        return '%s"%s":' % m.groups()
    s = "{a:1,b:2}"
    s2 = re.sub(r'([{,])(\w+):', replace, s)
    print s2


if __name__ == '__main__':
    # test()
    # test2()
    find_all_test2()
    # re_sub_test()