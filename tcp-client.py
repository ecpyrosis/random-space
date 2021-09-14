#!/usr/bin/env python

# tcp client 

import socket

#create client socket object
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
host = '192.168.56.10'
port = 4444

# c.connect(host,port)
c.connect((host,port))

message = c.recv(1024)

c.close()

print (message.decode('ascii'))

