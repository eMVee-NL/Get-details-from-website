#!/usr/bin/python3
import re

def printEmail(mails):
    mails = mails
    mail = []
    print("Email addresses found on the webpage")
    print("**********************************")
    for i in mails:
        if i not in mail:
            print("\t" + i)
            mail.append(i)
    print("**********************************\n")

def writeEmail(mails, hostname):
    mails = mails
    mail = []
    filename = hostname  + ".txt"
    f = open(filename, "a")
    f.write("Email addresses found on the webpage\n")
    f.write("**********************************\n")
    for i in mails:
        if i not in mail:
            f.write("\t" + i + "\n")
            mail.append(i)
    f.write("**********************************\n")
    f.close()

def getEmail(hostname, response):
    hostname = hostname
    req = response
    mails = set()  
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{2,7}", req.text, re.I))
    mails.update(new_emails)
    writeEmail(mails, hostname)
    printEmail(mails)