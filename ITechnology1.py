import sys, os
import getopt
from banner import *
from createProjectDirectory import createProjectDirectory
from getRobots import getRobots
from getHeaders import *
from hyperlinks import *
from comments import *
from metadata import *
from takeScreenshot import*

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, ITechnology requires Python 3.x\n")
    sys.exit(1)
  
def usage():
    print ("Usage:")
    print ("\t-u: url (http://www.website.com)")
    print ("\t-l: list (list.txt)\n")
    print ("example: python3 ITechnology.py -u http://www.website.com")
    print ("example: python3 ITechnology.py -l list.txt\n")

def start(argv):
    #Display banner
    displayBanner()
    path = os.path.abspath(os.curdir)
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "u:l")
    except getopt.GetoptError:
        print ("Error in arguments")
        sys.exit()
    for opt, arg in opts:
        if opt == '-u':
            url = arg
            print ("Target is set to: " + url + "\n")
        if opt == '-l':
            print ("a list in a file should be read")


if __name__ == "__main__":
    try:
        start(sys.argv[2:])
    except KeyboardInterrupt:
        print ("Session interrupted by user!!")