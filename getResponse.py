#!/usr/bin/python3
import requests

def getResponse(url, hostname):
    url = url
    filename = hostname
    # To do headers in request / random in the future
    # fix HTTPSConnectionPool(host='www.domainname.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
    agent = {"User-Agent":"Mozilla/60.0"}
    r = requests.get(url, headers=agent, verify=False)
    return r



