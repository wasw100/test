# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq

def get_content():
    url = 'http://www.douban.com/event/21309668/'
    r = requests.get(url)
    return r.text

def method_test():
    body = get_content()
    doc = pq(body)
    desc_pq = doc('#edesc_f')
    print desc_pq.text()
    print desc_pq.outerHtml()
    print desc_pq.html()

#todo selector by tag class id attr


if __name__ == '__main__':
    method_test()

