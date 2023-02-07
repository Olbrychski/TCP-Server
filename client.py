#!/usr/bin/python3
import sys
import socket
from socket import *

#Initialization, Create socket object
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#take input argument
host = sys.argv[1]

port = 3001

clientSocket.connect((host, port))
command =""

while True:
    command = input("Please enter a command: ")
    clientSocket.send(command.encode())
    message = clientSocket.recv(4064).decode()
    print (message)
    clientSocket.shutdown(SHUT_RDWR)
    clientSocket.close()

#print(msg.decode('ascii'))