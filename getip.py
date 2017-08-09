#!/usr/bin/python

from subprocess import Popen, PIPE
import re

def getIfconfig():
    p = Popen(['ifconfig'], stdout = PIPE)
    data = p.stdout.read().split('\n\n')
    return [i for i in data if i and not i.startswith('lo')]

def parseIfconfig(data):
#    dic = {}
#    for lines in data:
#        line_list = lines.split('\n')
#	devname = line_list[0].split()[0]
#	macaddr = line_list[0].split()[-1]
#	ipaddr = line_list[1].split()[1].split(':')[1]
#	dic[devname] = [ipaddr, macaddr]
#    return dic
    re_devname = re.compile(r'(br|eth|em|virbr|lo|bond)[\d:]+', re.M)
    re_mac = re.compile(r'HWaddr ([0-9A-F:]{17})', re.M|re.I)
    re_ip = re.compile(r'inet addr:([\d\.]{7,15})', re.M)
    devname = re_devname.search(data)
    if devname:
        devname = devname.group()
    else:
        devname = ''
    mac = re_mac.search(data)
    if mac:
        mac = mac.group(1)
    else:
        mac = ''
#    ip = re.re_ip.search(data).group()
    ip = re_ip.search(data)
    if ip:
        ip = ip.group(1)
    else:
        ip = ''
    return {devname:[ip, mac]}

if __name__ == '__main__':
    data = getIfconfig()
    for i in data:
        print parseIfconfig(i)
# print parseIfconfig(data)
