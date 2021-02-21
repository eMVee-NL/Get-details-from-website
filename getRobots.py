#!/usr/bin/python3
import sys, os, time
import wget
import requests
import http.client
from urllib.parse import urlparse

def readRobots(filename):
    print("\nDisplay the robots.txt file \n")
    print ("**********************************\n")
    try:
        file = open("robots.txt", "r")
        print (file.read())
    except:
        print ("Something went wrong!")

def getRobots(url):
    url = url
    file = "/robots.txt"
    workingDirectory = (url.split('//www.')[1])
    os.chdir('Collected-Data/'+ workingDirectory)
    time.sleep(1)
    print ("Trying to get the robots.txt file from: " + url)
    response = requests.get(url+file)
    if(response.status_code == 200):
        time.sleep(1)
        print ("The robots.txt file has been found on: " + url)
        print ("Trying to download: " +url + file)
        time.sleep(1)
        filename = wget.download(url + file)
        readRobots(filename)
        print ("**********************************\n")
