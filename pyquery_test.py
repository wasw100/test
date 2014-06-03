# -*- coding: utf-8 -*-

import re
import requests
from pyquery import PyQuery as pq

def get_content():
    url = 'http://www.douban.com/event/21299672/'
    r = requests.get(url)
    return r.text

def method_test():
    body = get_content()
    doc = pq(body)
    desc_pq = doc('#edesc_f')
    print desc_pq.text()
    print desc_pq.outerHtml()
    html = desc_pq.html()
    print html.replace('&#13;', '')

#todo selector by tag class id attr


def remove_html_tag():
    """test html_to_text"""
    content = '<span>123</span><br/><br/><div>hello<br>world<p>p</p>br1<br>br2<br/>br3<br /></div>'
    doc = pq(content)
    print doc.text()

    desc = html_to_text(content)
    print desc


TAG_RE = re.compile(r'<[^>]+>')


def _remove_or_replace_tag(match):
    """use for html_to_text"""
    if match.group().startswith(r'<br'):
        return '\n'
    else:
        return ''


def html_to_text(html):
    """replace <br> <br/> <br /> to \n, delete ohter tag"""
    return TAG_RE.sub(_remove_or_replace_tag, html)


def test_pq_remove():
    """
    eg: <p>hello me<span id="show_more">show more</span></p>
    to: <p>hello me</p>
    """
    s = '<div><p>hello me<span id="show_more">show more</span></p>good luck</div>'
    d = pq(s)
    d.remove('#show_more')
    print d.outerHtml()



if __name__ == '__main__':
    # method_test()
    # remove_html_tag()
    remove_tag_from_content()

