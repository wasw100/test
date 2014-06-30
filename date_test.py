# -*- coding: utf-8 -*-

import time
import datetime
import pytz
import calendar

def get_today_by_timezone(timestamp=time.time(), tz=pytz.timezone('Etc/GMT0')):
    """timezone day start time"""
    utc_now = pytz.utc.localize(datetime.datetime.utcfromtimestamp(timestamp))
    tz_now = tz.normalize(utc_now)
    t = int(timestamp - tz_now.hour * 3600 - tz_now.minute * 60 - tz_now.second)
    return t

def get_earliest_time(year, month, day):
    """the earliest time of one day in the word"""
    d = datetime.datetime(year, month, day)
    return calendar.timegm(d.timetuple()) - 12*3600

def get_day_start_time(timestamp, tz=pytz.timezone('Etc/GMT+12')):
    """the earliest time of one day in the word"""
    d1 = datetime.datetime.fromtimestamp(timestamp, tz=tz)
    print d1
    d2 = datetime.datetime(d1.year, d1.month, d1.day, tzinfo=tz)
    print d2
    return calendar.timegm(d2.timetuple()) - 12*3600


def show_the_last_10_day():
    tz = pytz.timezone('Etc/GMT-8')
    d = datetime.datetime.now(tz=tz)
    for i in range(10):
        d += datetime.timedelta(days=1)
        print d
        print d.strftime('%Y%m%d')

def test1():
    tz = pytz.timezone('Etc/GMT-12')
    # t1 = get_day_start_time(time.time(), tz)
    t1 = get_earliest_time(2014, 5, 20)
    t2 = get_today_by_timezone(time.time(), tz)
    print t1, t2, (t2-t1)/3600

def test2():
    tz = pytz.timezone("America/Los_Angeles")
    d = datetime.datetime(year=2014, month=7, day=1)
    d2 = tz.localize(d)
    print d
    print d2
    print calendar.timegm(d.utctimetuple())
    print calendar.timegm(d2.utctimetuple())


def test3():
    print pytz.country_timezones('cn')

    tz_cn = pytz.timezone('Asia/Shanghai')
    tz_utc = pytz.timezone('UTC')

    now = time.time()
    #系统时区的时间
    d = datetime.datetime.fromtimestamp(now)
    #d2是一个utc时区的时间
    d2 = datetime.datetime.utcfromtimestamp(now)

    print d
    print d2

    #将d1 d2加上自己的时区
    d_cn = tz_cn.localize(d)
    d_utc = tz_utc.localize(d2)

    print d_cn
    print d_utc

    #转换时区
    d_utc2 = d_cn.astimezone(tz_utc)
    print 'd_utc2', d_utc2

    #转换为unix timestamp
    print calendar.timegm(d_cn.utctimetuple())
    print calendar.timegm(d_utc.utctimetuple())

    print calendar.timegm(d_cn.timetuple())
    print calendar.timegm(d_utc.timetuple())


def tz_test():
    u = u'America/Los_Angeles'
    s = 'America/Los_Angeles'
    print pytz.timezone(u)
    print pytz.timezone(s)


if __name__ == '__main__':
    # show_the_last_10_day()
    # test3()
    tz_test()