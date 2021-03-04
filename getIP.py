#!/usr/bin/python3
import socket

def getIP(hostname):
    ipaddress = socket.gethostbyname(hostname)
    writeIP(hostname, ipaddress)
    printIP(hostname, ipaddress)

def checkIP(addr):
    try:
        socket.inet_aton(addr)
        # IP is correct
        return True
    except socket.error:
        # IP is incorrect
        return False

def writeIP(hostname, ipaddress):
    hostname = hostname
    ipaddress = ipaddress
    filename = hostname  + ".txt"
    f = open(hostname + "/" + filename, "a")
    f.write("IP address\n")
    f.write("**********************************\n")
    f.write("\t" + hostname + " : " + ipaddress + "\n")
    f.write("**********************************\n")
    f.close()

def printIP(hostname, ipaddress):
    hostname = hostname
    ipaddress = ipaddress
    print("IP address\n")
    print("**********************************\n")
    print("\t" + hostname + " : " + ipaddress + "\n")
    print("**********************************\n")