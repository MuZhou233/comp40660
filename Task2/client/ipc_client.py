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
    s.sendall(pickle.dumps({'command': 'ping'}))
    data = s.recv(1024)
    if data == b'pong':
        print('Connected to server')
        # random 50 numbers
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
        s.sendall(pickle.dumps({'command': 'exit'}))
    else:
        print('Failed to connect to server')

