# -*- coding: utf-8 -*-

import hashlib

def md5_test():
    s = '123' #202cb962ac59075b964b07152d234b70
    print hashlib.md5(s).hexdigest().lower()


def sha256_test():
    s = '123'
    print hashlib.sha256(s).hexdigest()


if __name__ == '__main__':
    # md5_test()
    sha256_test()
