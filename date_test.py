# -*- coding: utf-8 -*-

import time
import datetime
import pytz
import calendar

def get_today_by_timezone(tz):
    now = time.time()
    utc_now = pytz.utc.localize(datetime.datetime.utcfromtimestamp(now))
    tz_now = tz.normalize(utc_now)
    t = int(now - tz_now.hour * 3600 - tz_now.minute * 60 - tz_now.second)
    return t

def get_day_start_time(timestamp, tz=pytz.timezone('Etc/GMT+12')):
    d1 = datetime.datetime.fromtimestamp(timestamp, tz=tz)
    print d1
    d2 = datetime.datetime(d1.year, d1.month, d1.day, tzinfo=tz)
    print d2
    return calendar.timegm(d2.timetuple()) - 12*3600


if __name__ == '__main__':
    tz = pytz.timezone('Etc/GMT+12')
    t1 = get_day_start_time(time.time(), tz)
    t2 = get_today_by_timezone(tz)
    print t1, t2, (t2-t1)/3600
