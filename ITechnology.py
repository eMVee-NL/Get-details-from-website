import sys
import getopt
from banner import *
from createProjectDirectory import createProjectDirectory
from getRobots import getRobots
from headers import *
from hyperlinks import *
from comments import *
from metadata import *
from takeScreenshot import*
  
def usage():
    print ("Usage:")
    print ("\t-u: url (http://www.website.com)\n")
    print ("example: python3 ITechnology.py -u http://www.website.com\n")

def start(argv):
    #Display banner
    displayBanner()
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "u:")
    except getopt.GetoptError:
        print ("Error in arguments")
        sys.exit()
    for opt, arg in opts:
        if opt == '-u':
            url = arg
            print ("Target is set to: " + url + "\n")
            createProjectDirectory(url)
            takeScreenshot(url)
            getRobots(url)
            printing_headers(url)
            displayMetaData(url)
            displayHyperlinks(url)
            displayComments(url)

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print ("Session interrupted by user!!")