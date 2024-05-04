# !/usr/bin/env python3
# ipc_server.py
# Base https://medium.com/techanic/docker-containers-ipc-using-sockets-part-1-2ee90885602c

import socket

HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9898  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
