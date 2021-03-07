#!/usr/bin/python3
import validators, socket, tldextract, os
from createWorkingDirectory import * 
from takeScreenshot import *
from getRobots import *
from getIP import *
from getResponse import *
from getHeaders import *
from getMetadata import *
from getEmail import *
from getHyperlinks import *
from getComments import *

def getAllData(hostname, url, path):
    print("Create directory " + hostname)
    createWorkingDirectory(path, hostname)
    takeScreenshot(url, hostname)
    print("Create file: " + hostname + ".txt\n")
    f = open(hostname + "/" + hostname  +".txt", "a")
    f.close()
    getIP(hostname)
    getRobots(url, hostname)
    #getResponse, in this module the random user agent should be created in the future
    response = getResponse(url, hostname)
    getHeaders(hostname, response)
    getMetadata(hostname, response)
    getEmail(hostname, response)
    getHyperlinks(hostname, response)
    getComments(hostname, response)

def checkURL(path, url):
    path = path
    url = url
    valid=validators.url(url)
    if valid==True:
        print("\n" + url + " is a valid url, let's collect more information!\n")
        ext = tldextract.extract(url)
        # If url is an IP address print IP address
        if checkIP(ext.domain) == True and ext.suffix == '':
            hostname = ext.domain
            getAllData(hostname, url, path)
        # IF ext.subdomain =! null && =! wwww
        elif ext.subdomain not in ('', 'www', 'www1', 'www2', 'www3'):
            hostname = '.'.join(ext[:3])
            getAllData(hostname, url, path)
        # IF ext.subdomain = www(x)
        elif ext.subdomain in ('www', 'www1', 'www2', 'www3'):
            hostname = '.'.join(ext[:3]) 
            getAllData(hostname, url, path)
        # If url is registered_domain print IP with gethostbyname
        else:
            hostname = ext.registered_domain
            getAllData(hostname, url, path)
    else:
        print(url + " is an invalid url")



path = os.path.abspath(os.curdir)
checkURL(path, 'www.9292.nl')