# -*- coding: utf-8 -*-

def set_test():
    s = set('abc')
    s2 = {v for v in 'abc'}
    print s, s2
    print 'b' in s
    s.add('d')
    print s
    s.remove('b')
    #s.remove('s') raise KeyError
    print s
    s.discard('a') #如果存在就移除
    print s
    s.discard('s')
    print s


def check_str():
    u = u'abc'
    s = 'abc'
    print isinstance(u, str)
    print isinstance(s, str)


if __name__ == '__main__':
    # set_test()
    check_str()
