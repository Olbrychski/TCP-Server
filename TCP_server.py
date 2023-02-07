#!/usr/bin/python3

import sys
import socket
import threading


N = 20 # max number of clients

# Server initialization, Creating the socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse socket
host = sys.argv[1]

#Bind to socket
serverSocket.bind((host, 3001)) # Host ip and port to be used
serverSocket.listen() # start TCP listener

# Keep track of connected clients and ranks
clients = set()
ranks = {} 


def client_handle(client):
    # Assign rank to client
    rank = 0
    for r in ranks.values():
        if r >= rank:
            rank = r + 1
    ranks[client] = rank
    print(f'Client {client.getpeername()} assigned rank {rank}')

    while True:
        # Receive command from client
        command = client.recv(4064).decode()
        if not command:
            break

        # Check if client has permission to execute command
        sender_rank = ranks[client]
        for k in clients:
            if ranks[k] < sender_rank:
                k.send(command)
                print(f'Command executed by client {k.getpeername()}')

    # Remove client and adjust ranks
    clients.remove(client)
    del ranks[client]
    for k in clients:
        if ranks[k] > rank:
            ranks[k] -= 1


    name = str(client.getpeername())      
    client.close()
    print('Client ' + name + ' disconnected')
# Add connected client and start new thread
while True:
    client, addr = serverSocket.accept()
    print(f'Connected by {addr}')
    clients.add(client)
    client_thread = threading.Thread(target=client_handle, args=(client,))
    client_thread.start()
    command = input("Please enter a command: ")
