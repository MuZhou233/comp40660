# !/usr/bin/env python3
# ipc_server.py
# Base https://medium.com/techanic/docker-containers-ipc-using-sockets-part-1-2ee90885602c

import socket
import pickle

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
            data = pickle.loads(data)
            match data['command']:
                case 'exit':
                    break
                case 'ping':
                    conn.sendall(b'pong')
                case 'math':
                    numbers = data['numbers']
                    res = {
                        'mean': sum(numbers) / len(numbers),
                        'median': sorted(numbers)[len(numbers) // 2],
                        'standard_deviation': (sum((x - sum(numbers) / len(numbers)) ** 2 for x in numbers) / len(numbers)) ** 0.5
                    }
                    conn.sendall(pickle.dumps(res))
                case 'light':
                    lux = data['lux']
                    time = data['time']
                    curtain = 'open'
                    light = 'on'
                    if time < 6:
                        curtain = 'closed'
                        light = 'off'
                    elif time < 8 or time > 20:
                        curtain = 'closed'
                        light = 'on' if lux < 100 else 'off'
                    else:
                        curtain = 'open' if lux < 500 else 'closed'
                        light = 'on' if lux < 100 else 'off'
                    conn.sendall(pickle.dumps({
                        'curtain': curtain,
                        'light': light
                    }))
                case _:
                    conn.sendall(b'Unknown command')
