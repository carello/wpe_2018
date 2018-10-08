# client
# !/usr/bin/env python3

import socket


serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
serversocket.bind((host, port))

serversocket.listen()
print("Ready to accept connection")

clientsocket, addr = serversocket.accept()

actions = {
    'say': lambda word: word,
    'increment': lambda x: str(int(x) + 1)
}

while True:
    client_message = clientsocket.recv(1024).decode()

    if not client_message:
        break

    print(f"Received: '{client_message}'")

    command, *args = client_message.split()

    if command == 'bye':
        break
    elif command not in actions:
        clientsocket.send(f"Unknown command '{client_message}'".encode())
    else:
        clientsocket.send(actions[command](' '.join(args)).encode())

clientsocket.close()
