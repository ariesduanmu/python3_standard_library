# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-22 16:54:15
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-22 17:07:14
import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

server.listen(5)

