# -*- coding: utf-8 -*-
"""
google calendar repeat event parse
"""
import re
import pytz
import datetime
import dateutil.rrule
import dateutil.parser

EXDATE_PATTERN = re.compile(r'EXDATE;TZID=([^:]+):(.+)')


def test():
    recurrence = ["EXDATE;TZID=Asia/Shanghai:20141226T140000,20141230T140000",
                  "RRULE:FREQ=DAILY;COUNT=30"]
    r_set = dateutil.rrule.rruleset()
    tz_china = pytz.timezone('Asia/Shanghai')
    start_d = datetime.datetime(2014, 12, 20, 14)
    start_d = tz_china.localize(start_d)
    for s in recurrence:
        if s.startswith('RRULE'):
            rrule = dateutil.rrule.rrulestr(s, dtstart=start_d)
            r_set.rrule(rrule)
        elif s.startswith('EXDATE'):
            m = EXDATE_PATTERN.match(s)
            if m:
                tz_name = m.group(1)
                tz = pytz.timezone(tz_name)
                for date_str in m.group(2).split(','):
                    d = dateutil.parser.parse(date_str)
                    d = tz.localize(d)
                    r_set.exdate(d)
        else:
            raise Exception("Can't parse rule:{}".format(s))

    for r_d in r_set:
        print r_d


if __name__ == '__main__':
    test()
