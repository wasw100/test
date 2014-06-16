# -*- coding: utf-8 -*-
"""
网页内容解析
1.正则
2.pyquery
3.xpath
"""

import lxml.html
import re

html = """
<!doctype html>
<html><body>
<div id="content">
<ul class="nav">
<li><a href="http://test.com/post/1" target="_blank">1</a></li>
<li><a href="http://test.com/post/2" target="_blank">2</a></li>
<li><a href="http://test.com/post/3" target="_blank">3</a></li>
<li><a href="http://test.com/post/4" target="_blank">4</a></li>
<li><a href="http://test.com/post/5" target="_blank">5</a></li>
<ul>
<div>
</body><html>
"""


HREF_PATERN = re.compile('href="(http://test.com/post/(\d+))"')
def re_test():
    """parse use re"""
    print HREF_PATERN.findall(html)


def pyquery_test():
    """parse use pyquery"""
    pass


def xpath_test():
    """parse use xpath"""
    dom = lxml.html.fromstring(html)
    hrefs = dom.xpath('//*[@id="content"]/ul/li[*]/a')
    print len(hrefs)
    for href in hrefs:
        print href.attrib
        print href.text


if __name__ == '__main__':
    re_test()
    # xpath_test()



