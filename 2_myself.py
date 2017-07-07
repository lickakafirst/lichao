#!/usr/bin/python
#coding=utf-8

import urllib, urllib2
import re

#获取网页信息
def getPageInformation(url):
    pageRequest = urllib2.Request(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'})
    pageTxt = urllib2.urlopen(pageRequest)
    return pageTxt.read()

#正则匹配获取想要的内容
def getPageTxt(html):
    txtRe = re.compile(r'<div class="author.*?".*?<img.*?alt="(.*?)".*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>', re.S)
    txtList = txtRe.findall(html)
    print txtList
    for items in txtList:
        for item in items:
	    print item

if __name__ == "__main__":
    url = 'https://www.qiushibaike.com/8hr/page/2/?s=4998161'
    html = getPageInformation(url)
    getPageTxt(html)
    
