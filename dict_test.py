# -*- coding: utf-8 -*-


def delete_key1():
    d = dict(a=1, b=2)
    print d
    del d['a']
    print d

def delete_key2():
    d = dict(a=1, b=2)
    print d
    del d['a']
    #raise KeyError,
    # del d['c']

    #SyntaxError: can't delete function call
    # del d.get('a')
    print d


def delete_key3():
    d = dict(a=1, b=2)
    #raise KeyError: 'c'
    # d.pop('c')
    d.pop('a')

    print d


def delete_key4():
    d = dict(a=1, b=2)
    if 'c' in d:
        del d['c']

    d.pop('c', None)
    d.pop('a', None)
    print d

if __name__ == '__main__':
    delete_key4()