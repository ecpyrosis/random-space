#!/usr/bin/env python

# use socket to grab banner

import socket
# s = socket.socket()
# ip = input("Plase entere IP: ")
# port = str(input("Plese enter a Port: "))
# s.connect(ip, int(port))
# print(s.recv(1024))

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input('Please enter IP: ')
    port = str(input('Please enter the Port: '))
    banner(ip, port)

main()
