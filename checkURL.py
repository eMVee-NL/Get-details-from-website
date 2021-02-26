import validators
import socket
import tldextract

def checkURL(url):
    url = url
    valid=validators.url(url)
    if valid==True:
        print (url + " has valid url")
        # If url is an IP address print IP address

        # If url is registered_domain print IP with gethostbyname
        print ("IP: " + socket.gethostbyname(hostname))
    else:
        print (url + "has invalid url")

print ("IP: " + socket.gethostbyname('sub.website.com'))
print ("IP: " + socket.gethostbyname('website.com'))
#ext = tldextract.extract("http://www.website.com/")
ext = tldextract.extract('http://IP')
print (ext.subdomain, ext.domain, ext.suffix)
print (ext.registered_domain)


checkURL("IP")
checkURL("sub.domain.com")
