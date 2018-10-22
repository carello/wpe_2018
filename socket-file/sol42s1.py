#!/usr/bin/env python3

import socket
import pickle
import glob

actions = {}

for one_filename in glob.glob("server_func*.py"):
    print(f"Now reading {one_filename}")
    exec(open(one_filename).read(), actions)

print(f"Available commands: {actions.keys()}")

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
host = 'localhost'
serversocket.bind((host, port))

serversocket.listen()
print("Ready to accept connection")

clientsocket, addr = serversocket.accept()

while True:
    client_message = clientsocket.recv(1024).decode()

    if not client_message:
        break

    print(f"Received: '{client_message}'")

    command, *args = client_message.split()

    if command == 'bye':
        break
    elif command not in actions:
        clientsocket.send(pickle.dumps(f"Unknown command '{client_message}'"))
    else:
        clientsocket.send(pickle.dumps(actions[command](*args)))

clientsocket.close()
