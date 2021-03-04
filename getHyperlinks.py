#!/usr/bin/python3
from bs4 import BeautifulSoup

def writeHyperlinks(hostname, soup):
    soup = soup
    filename = hostname  + ".txt"
    f = open(filename, "a")
    f.write("Hyperlinks found on the webpage\n")
    f.write("**********************************\n")
    for link in soup.find_all("a"):
        f.write("\tInner Text: {}".format(link.text) + "\n")
        f.write("\tTitle: {}".format(link.get("title")) + "\n")
        f.write("\tHref: {}".format(link.get("href")) + "\n")
        f.write("\t================================" + "\n")
    f.write("**********************************\n")
    f.close()

def printHyperlinks(soup):
    soup = soup
    print ("Hyperlinks found on the webpage")
    print ("**********************************")
    for link in soup.find_all("a"):
        print ("\tInner Text: {}".format(link.text))
        print ("\tTitle: {}".format(link.get("title")))
        print ("\tHref: {}".format(link.get("href")))
        print ("\t================================")
    print ("**********************************\n")


def getHyperlinks(hostname, response):
    hostname = hostname
    html_content = response.text 
    soup = BeautifulSoup(html_content, "lxml")
    writeHyperlinks(hostname, soup)
    printHyperlinks(soup)    