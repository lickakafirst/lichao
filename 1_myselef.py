#!/usr/bin/python
#coding=utf-8
#爬虫，获取网页图片

import urllib, urllib2
import re

#函数获取网页源码
def getHtml(url):
    img_url = urllib2.urlopen(url)
    return img_url.read()

#正则表达式匹配网页中的要爬去的内容，以列表的方式存储，并打印出来
def getImage(html):
    i = 1
    img_re = re.compile(r'img class="BDE_Image" src="(.*?)".*?>')
    img_list = img_re.findall(html)
    for imgurl in img_list:
        print imgurl
        urllib.urlretrieve(imgurl, filename = "%s.jpg" % i)
	i += 1

if __name__ == "__main__":
    url = 'https://tieba.baidu.com/p/5207860131'
    imgresult = getHtml(url)
    getImage(imgresult)
