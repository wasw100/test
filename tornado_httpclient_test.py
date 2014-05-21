# -*- coding: utf-8 -*-
import datetime
from tornado import gen
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')

def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body

def test1():
    """test callback"""
    print 'test1'
    http_client = AsyncHTTPClient()
    http_client.fetch("http://www.baidu.com/", handle_request)

@gen.coroutine
def test2():
    """test return data"""
    print 'test2'
    response = yield return_data()
    print response.body

@gen.coroutine
def return_data():
    client = AsyncHTTPClient()
    response = yield client.fetch("http://www.baidu.com/")
    raise gen.Return(response)

@gen.coroutine
def test3():
    """loop request url"""
    response = yield return_data()
    print datetime.datetime.now(), response.body
    tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=5), test3)

def start():
    """start ioloop"""
    tornado.ioloop.IOLoop().instance().start()

if __name__ == '__main__':
    test3()
    tornado.ioloop.IOLoop().instance().start()
