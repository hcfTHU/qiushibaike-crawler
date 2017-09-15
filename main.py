# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 10
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=10)
    # print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

content = response.read().decode('utf-8')
pattern = re.compile(r'<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                     r'content">(.*?)<!--(.*?)-->(.*?)</div>',re.S)
items = re.findall(pattern, content)
for item in items:
    # print item[3]
    if re.search(r'img', item[3]):
        pass
    else:
        # print item[1]
        target = re.search(r'<span>(.*?)</span>', item[1], re.S)
        print target.group(1)

