#!/usr/bin/python3
import requests

def writeHeaders(response, hostname):
    r = response
    filename = hostname  + ".txt"
    f = open(filename, "a")
    f.write ("Server headers\n")
    f.write ("**********************************\n")
    for x in r.headers:
        f.write('\t' + x + ' : ' + r.headers[x] + '\n')
    f.write ("**********************************\n")
    f.close()

def printHeaders(response):
    r = response
    print ("Server headers")
    print ("**********************************")
    for x in r.headers:
        print ('\t' + x + ' : ' + r.headers[x])
    print ("**********************************\n")

def getHeaders(hostname, response):
    filename = hostname
    r = response
    # To do headers in request / random in the future
    # fix HTTPSConnectionPool(host='www.domainname.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
    agent = {"User-Agent":"Mozilla/60.0"}
    #r = requests.get(url, headers=agent, verify=False)
    writeHeaders(r, hostname)
    printHeaders(r)