#!/usr/bin/python
#coding=utf-8

import sys
import string
import os

#定义函数判定字符串为数字还是字符
#判断字符串每一个元素是不是由数字构成
def isNum(s):
    for i in s:
	if i in string.digits:
	    continue
	else:
	    return False
    return True
for pid in os.listdir('/proc'):
    if isNum(pid):
        print pid
