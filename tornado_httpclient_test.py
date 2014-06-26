# -*- coding: utf-8 -*-
import datetime
from tornado import gen
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient', max_clients=2)

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


#add test for max_clients, proxy, and calback
def callback(response):
    print response.time_info

def test4():
    request = HTTPRequest('http://www.163.com', proxy_host='http://127.0.0.1', proxy_port=8888)
    for i in range(10):
        AsyncHTTPClient().fetch(request, callback=callback)

if __name__ == '__main__':
    test4()
    tornado.ioloop.IOLoop().instance().start()
