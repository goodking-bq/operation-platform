# coding:utf-8
from __future__ import absolute_import, unicode_literals

__author__ = "golden"
__date__ = '2017/9/29'


def tcp():
    import requests

    req = requests.get('http://kksk.org/tieku/r_1258_80.html', proxies={
        'http': 'socks5://@45.249.245.27:22873',
        # 'https': 'socks5://user:pass@host:port'
    })
    print(req.content)


def udp():
    import socket
    import socks
    socks.set_default_proxy(socks.SOCKS5, port=8888, addr='192.168.2.41', username='golden', password='golden')
    socket.socket = socks.socksocket
    address = ('www.baidu.com', 80)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'aa', address)
    print(s.recv(1024))
    print('aa')


if __name__ == '__main__':
    udp()
