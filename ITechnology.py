#!/usr/bin/env python3
import sys, os, shutil
from banner import *
from checkURL import checkURL

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, ITechnology requires Python 3.x\n")
    sys.exit(1)

def runTheProgram(path, url):
    checkURL(path, url)

def openFile(filename):
    print("Open File " + filename)
    print("This function is not yet developed!")
    #runTheProgram(name)

def usage():
    print ("Usage:")
    print ("\t-h: help")
    print ("\t-u: url (http://www.website.com)")
    print ("\t-l: list (list.txt)\n")
    print ("example: python3 ITechnology.py -u http://www.website.com")
    print ("example: python3 ITechnology.py -l list.txt\n")

def removePyCache(path):
    directory = "__pycache__"
    path = path + "/"
    try:
        shutil.rmtree(path + directory)
    except OSError as e:
        print("Error: %s : %s" % (path + directory, e.strerror))

def main():
    displayBanner()
    args = sys.argv[1:]
    path = os.path.abspath(os.curdir)
    # check for the -u argument indicating to run against one website
    if len(args) == 2 and args[0] == '-u':
        runTheProgram(path, args[1])
    # Check for the -l argument indicating to read the file line for line with domains
    if len(args) == 2 and args[0] == '-l':
        openFile(args[1])
    # Check for -h argument to show options (help function)
    if len(args) == 1 and args[0] == '-h':
        usage()
    if len(args) == 0:
        usage()
    removePyCache(path)
    


# Run the whole thing.
if __name__ == '__main__':
    main()