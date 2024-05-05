#!/usr/bin/env python3
# ipc_client.py
# Base https://medium.com/techanic/docker-containers-ipc-using-sockets-part-1-2ee90885602c

import socket
import pickle
import random

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Ping server')
    s.sendall(pickle.dumps({'command': 'ping'}))
    data = s.recv(1024)
    if data == b'pong':
        print('Connected to server')

        print('Requesting math operation')
        numbers = []
        for i in range(50):
            numbers.append(random.randint(1, 100))
        print('Sending', numbers)
        s.sendall(pickle.dumps({
            'command': 'math',
            'numbers': numbers,
        }))
        data = s.recv(1024)
        print('Received', repr(pickle.loads(data)))

        print('Requesting light operation')
        for i in range(5):
            lux = random.randint(1, 300)
            time = random.randint(0, 24)
            print('Sending current sates. lux:', lux, ', hour', time)
            s.sendall(pickle.dumps({
                'command': 'light',
                'lux': lux,
                'time': time,
            }))
            data = s.recv(1024)
            print('Received', repr(pickle.loads(data)))
        print('Closing connection')
        s.sendall(pickle.dumps({'command': 'exit'}))
    else:
        print('Failed to connect to server')
    print('Connection closed')
