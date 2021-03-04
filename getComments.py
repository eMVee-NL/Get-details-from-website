#!/usr/bin/python3
from bs4 import BeautifulSoup
from bs4 import Comment

def writeComments(hostname, response):
    html_content = response.text
    soup = BeautifulSoup(html_content, "lxml")
    filename = hostname  + ".txt"
    f = open(filename, "a")
    f.write("Comments found in the source code\n")
    f.write("**********************************\n")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        f.write("\t" + c + "\n")
        f.write("\t================================\n")
        c.extract()
    f.write("**********************************\n")

def printComments(response):
    html_content = response.text
    soup = BeautifulSoup(html_content, "lxml")
    print("Comments found in the source code")
    print("**********************************")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        print("\t" + c)
        print("\t================================")
        c.extract()
    print ("**********************************\n")

def getComments(hostname, response):
    hostname = hostname
    response = response
    writeComments(hostname, response)
    printComments(response)