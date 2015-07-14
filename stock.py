__author__ = 'z97'

import requests


def test():
    rt=requests.get("http://hq.sinajs.cn/list=s_sh000001")
    print(rt.text)

def test2():
    yahoo="http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=25&c=2010&d=09&e=8&f=2010&g=d"
    yahoo2="http://table.finance.yahoo.com/table.csv?s=600000.SS&d=6&e=22&f=20015&g=d&a=11&b=16&c=2014&ignore=.csv"


    yahoo3="http://table.finance.yahoo.com/table.csv?s={0}&d=6&e=22&f=20015&g=d&a=11&b=16&c=2014&ignore=.csv"
    rt=requests.get(yahoo3.format("600010.SS"))
    print(rt.text)

test2();