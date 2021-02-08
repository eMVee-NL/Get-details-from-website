import requests


def printing_headers(url):
    url = url
    agent = {"User-Agent":"Mozilla/60.0"}
    r = requests.get(url, headers=agent, verify=False)
    print ("Server headers")
    print ("**********************************")
    for x in r.headers:
        print ('\t' + x + ' : ' + r.headers[x])
    print ("**********************************\n")

#HTTPSConnectionPool(host='www.domainname.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
