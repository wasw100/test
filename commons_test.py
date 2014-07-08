# -*- coding: utf-8 -*-
import  os.path

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


def path_join_test():
    """
    使用os.path.join 第二个参数一般情况下是一个相对路径
    :return:
    """
    print '__file__:', __file__
    cur_path = os.path.dirname(__file__)
    print 'cur_path', cur_path
    join_path = os.path.join('/Users/w3/Documents/github/', '/ddd')
    print join_path
    join_path2 = os.path.join('/Users/w3/Documents/github/', 'ddd')
    print join_path2


if __name__ == '__main__':
    # set_test()
    # check_str()
    path_join_test()