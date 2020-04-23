# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-23 18:25:31
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-23 18:33:26
# 11.4.1 Using select()

import socket
import sys

messages = [
'This is the message. ',
'It will be sent ',
'in parts. ',
]

server_address = ('localhost', 10001)

socks = [
socket.socket(socket.AF_INET, socket.SOCK_STREAM),
socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

print('connecting to {} port {}'.format(*server_address), file=sys.stderr)
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()
    for s in socks:
        print(f'{s.getsockname()}: sending {outgoing_data}', file=sys.stderr)
        s.send(outgoing_data)

    for s in socks:
        data = s.recv(1024)
        print(f'{s.getsockname()}: received {data}', file=sys.stderr)

        if not data:
            print(f'close socket {s.getsockname()}', file=sys.stderr)
            s.close()