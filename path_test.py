# -*- coding: utf-8 -*-

import glob
import os.path

def test():
    print os.path.join(os.path.dirname(__file__), 'logging.conf')


def os_walk_test():
    """
    doc: https://docs.python.org/2/library/os.html
    os.walk use
    os.walk return a generator object walk

    """
    path = os.path.dirname(__file__)
    print 'path', path
    #迭代每个item是一个长度为3的tuple, 0:path 1.dir list 2.filename list
    #遍历一个目录下的所有.py文件,可以这么处理
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            print filename


def glob_test():
    """路径下所有的py文件"""
    path = os.path.dirname(__file__)
    s = os.path.join(path, '*.py')
    print glob.glob(s)


if __name__ == '__main__':
    # test()
    # os_walk_test()
    glob_test()