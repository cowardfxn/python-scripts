#!/usr/bin/python
# encoding: utf-8

'''
socket server/client设置
说明在最后
'''

import socket, string
from random import choice
from time import sleep

# URLS = '127.0.0.1', 29999
URLS = 'localhost', 29999

def run(interval=1):
    conts = list(string.uppercase)
    socket_server = socket.socket()
    socket_server.bind(URLS)
    socket_server.listen(1)
    conn, addr = socket_server.accept()
    try:
        while 1:
            r = choice(conts) + "\n"
            r = r.encode('utf-8')
            rslt = conn.send(r, len(r))
            if rslt:
                print('Character "{}" is sent.'.format(r))
                sleep(interval)
    except Exception as e:
        print(e)
    finally:
        conn.close()
        socket_server.close()

if __name__ == '__main__':
    run()

'''
sudo ufw disable
sudo apt-get install telnetd
cat /etc/inetd.conf
telnet    stream  tcp     nowait  telnetd /usr/sbin/tcpd  /usr/sbin/in.telnetd
sudo service inetd restart
netstat -nltp | grep telnet


iptables -A OUTPUT -p tcp --sport 29999 -j ACCEPT
iptables -A INPUT -p tcp --dport 29999 -j ACCEPT

对于socket，必须先在server端开启监听，然后client端才能开启连接，传输数据
上面关于socket的认识有误，当需要从server端获取数据时，应该是server端通过socket发送数据出去，
而不是另外建立client，向server发送数据进去
server端和client端的对象虽然都是叫做socket，但是client端使用socket.socket返回的对象进行读写操作，server端的socket对象只有绑定端口，建立连接的作用，
bind之后，使用socket.socket对象accept方法返回的连接进行读写操作，需要注意，两方使用的方法不同
'''
