# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-22 16:54:15
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-23 18:33:32
# 11.4.1 Using select()

import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10001)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

server.listen(5)

inputs = [server]

outputs = []

message_queues = {}

while inputs:
    print('waiting for the next event', file=sys.stderr)
    # The first is a list of the objects to be checked for incoming data to be read, 
    # the second contains objects that will receive outgoing data when there is room in their buffer, 
    # and the third includes those objects that may have an error (usually a combination of the input and output channel objects). 
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    if not (readable or writable or exceptional):
        print('  timed out, do some other work here', file=stderr)
        continue

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print(f'  connection from {client_address}', file=sys.stderr)

            connection.setblocking(0)
            inputs.append(connection)

            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print(f'  received {data} from {s.getpeername()}', file=sys.stderr)

                if s not in outputs:
                    outputs.append(s)

            else:
                print(f' closing {client_address}', file=sys.stderr)
                if s in outputs:
                    outputs.remove(s)

                inputs.remove(s)
                s.close()

                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print(f'  {s.getpeername()} queue empty', file=sys.stderr)
            outputs.remove(s)
        else:
            print(f'  sending {next_msg} to {s.getpeername()}', file=sys.stderr)
            s.send(next_msg)

    for s in exceptional:
        print(f'exception condition on {server.getpeername()}', file=sys.stderr)

        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]