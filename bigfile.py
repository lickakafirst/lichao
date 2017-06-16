#!/usr/bin/python
#coding=utf-8

import os
import operator
import sys

def get_filesize(topdir):
    dic = {}  #定义字典，key = filename，value = filesize 
    a = os.walk(topdir) # 记住os.walk,目录遍历
    for fpath, fdir, fname in a:
        for i in fname:
	    fn = os.path.join(fpath, i)
	    f_size = os.path.getsize(fn) #得到filesize
	    dic[fn] = f_size
    return dic

if __name__ == "__main__":
    dic =  get_filesize(sys.argv[1])
# key为sorted函数关键字，并字典key，operator.itemgetter(0|1),选择根据字典的key还是value
    sorted_dic = sorted(dic.iteritems(), key = operator.itemgetter(1), reverse = True)
#   print sorted_dic
    for k, v in sorted_dic[:10]:
        print k,'--->', v
