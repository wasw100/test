# -*- coding: utf-8 -*-
"""
网页内容解析
1.正则
2.pyquery
3.xpath
xml.etree.ElementTree — The ElementTree XML API
https://docs.python.org/2/library/xml.etree.elementtree.html
"""

import lxml.html
import re
from pyquery import PyQuery as pq

html = """
<!doctype html>
<html><body>
<div id="content">
<ul class="nav">
<li><a href="http://test.com/post/1" target="_blank">1</a></li>
<li><a flag="1" href="http://test.com/post/2" target="_blank">2</a></li>
<li><a href="http://test.com/post/3" target="_blank">3</a></li>
<li><a flag="1" href="http://test.com/post/4" target="_blank">4</a></li>
<li><a href="http://test.com/post/5" target="_blank">5</a></li>
<ul>
<div>
<div flag="1">div</div>
</body><html>
"""


HREF_PATERN = re.compile('href="(http://test.com/post/(\d+))"')
def re_test():
    """parse use re"""
    print HREF_PATERN.findall(html)


def pyquery_test():
    """parse use pyquery"""
    d = pq(html)
    for ele in d('li a'):
        print ele.attrib
        print ele.text


def xpath_test():
    """parse use xpath"""
    dom = lxml.html.fromstring(html)
    eles = dom.xpath('//*[@id="content"]/ul/li[*]/a')
    print len(eles)
    for ele in eles:
        print ele.attrib
        print ele.text


def xpath_attr_test():
    dom = lxml.html.fromstring(html)
    eles = dom.xpath('//a[@flag="1"]')
    for ele in eles:
        print ele.attrib
        print ele.text


def pyquery_attr_test():
    d = pq(html)
    for ele in d('a[flag="1"]'):
        print ele.attrib
        print ele.text


if __name__ == '__main__':
    # re_test()
    # pyquery_test()
    # xpath_test()
    # xpath_attr_test()
    pyquery_attr_test()


