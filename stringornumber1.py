#!/usr/bin/python
#coding=utf-8

#利用字符串方法判断字符串为数字还是字符
import os

for pid in os.listdir('/proc'):
    if  pid.isdigit():
	print pid
