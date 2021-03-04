#!/usr/bin/python3
from bs4 import BeautifulSoup

def writeMetadata(hostname, soup):
    soup = soup
    filename = hostname  + ".txt"
    f = open(filename, "a")
    f.write("Metadata of the website\n")
    f.write("**********************************\n")
    try:
        f.write("\tTitle of website: ", soup.title.text + "\n")
    except:
        f.write("\tThe title could not be found\n")
    f.write("**********************************\n")
    f.write("Meta data of the website\n")
    f.write("**********************************\n")
    meta = soup.find_all('meta')
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords', 'generator']:
            f.write('\tName    :' + tag.attrs['name'].lower() + '\n')
            f.write('\tContent :' + tag.attrs['content'] + '\n')
    f.write("**********************************\n")
    f.close()

def printMetadata(soup):
    soup = soup
    print ("Metadata of the website")
    print ("**********************************")
    try:
        print ("\tTitle of website: ", soup.title.text)
    except:
        print ("\tAn exception occurred, the title could not be found!")
    print ("**********************************\n")
    print ("Meta data of the website")
    print ("**********************************")
    meta = soup.find_all('meta')
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords', 'generator']:
            print ('\tName    :',tag.attrs['name'].lower())
            print ('\tContent :',tag.attrs['content'])
    print ("**********************************\n")

def getMetadata(hostname, response):
    hostname = hostname
    response = response
    html_content = response.text
    soup = BeautifulSoup(html_content, "lxml")
    writeMetadata(hostname, soup)
    printMetadata(soup)