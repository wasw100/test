# -*- coding: utf-8 -*-
"""
test https://github.com/gitpython-developers/GitPython
tutorial https://pythonhosted.org/GitPython/0.3.2/tutorial.html
"""

from git import Repo


def test_pull():
    """ 只用到git pull, 测试git pull"""
    repo = Repo("/Users/w3/data/github/webpy")
    origin = repo.remotes.origin
    print origin.pull()


if __name__ == '__main__':
    test_pull()