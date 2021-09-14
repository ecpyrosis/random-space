#!/usr/bin/env python

# create a tcp server 

import socket

#create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 4444

# bind object with values abolve
s.bind((host, port))

# set up tcp listener
# how many connections/requests allowd on listener at a time
s.listen(3)

# c = client socket object
while True:
    c, address = s.accept()
    print("recieved connection from %r " % str(address))

    message = 'hello! thank you for connecting to the server '
    c.send(message)
    # c.send(message.encode('ascii'))

    c.close()