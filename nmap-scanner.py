#!/usr/bin/env python

# nmap like scanner for macos

# brew install nmap
# pip3 install python3-nmap

import nmap

scanner = nmap.PortScanner()

print("Welcome to the jungle baby!")
print("---------------------------------->")

ip_addr = input("Enter an IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# https://docs.python.org/3/library/functions.html?highlight=type#type
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
             1) SYN ACK scan
             2) UDP scan
             3) Comprehensive scan \n""")
print("You selected option: ", resp)

if resp == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

# else resp >= '4':
#     print("Please enter a valid option (1-3)")

else:
    print("Please enter a valid option (1-3)")
