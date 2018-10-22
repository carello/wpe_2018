#!/usr/bin/env python3

import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
host = 'localhost'
s.connect((host, port))

# Receive no more than 1024 bytes

s.send('numbers_this'.encode())
msg = pickle.loads(s.recv(1024))
print(f"1 - Response: {msg}")
print(f"Response type: {type(msg)}")
print()

s.send('reverse_word hello'.encode())
msg = pickle.loads(s.recv(1024))
print(f"2- Response: {msg}")
print(f"Response type: {type(msg)}")
print()

s.send('unicode_map exponentiation'.encode())
msg = pickle.loads(s.recv(1024))
print(f"3- Response: {msg}")
print(f"Response type: {type(msg)}")
print()

s.send('this is garbage!'.encode())
msg = pickle.loads(s.recv(1024))
print(f"4- Response: {msg}")
print(f"Response type: {type(msg)}")
print()
