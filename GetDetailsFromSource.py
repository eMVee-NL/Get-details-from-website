# This script reads some parts of the source code from a website. It collects the title, meta data, comments and hyperlinks.
# To use this script, the following should be installed on the system: requests beautifulsoup4 lxml
# To install the required software you should run the command wirtten below
# pip3 install requests beautifulsoup4 lxml
# To run this scrpit you have to run it like GetSource.py https://www.website.com or GetSource.py http://www.website.com

# importing the libraries
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import sys
if len (sys.argv) != 2 :
    print ("Usage: python GetSource.py https://www.website.com or GetSource.py http://www.website.com ")
    sys.exit (1)


print ("#########################################################")
print ("# Running script: ", sys.argv[0], "                        #")
print ("# This script is created by Matthijs van der Vaart      #")
print ("#########################################################")
print ()
url = sys.argv[1]
#url=input()

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

#Print the title of the webpage
print ()
print ("#########################################################")
print ("# The title of the webpage                              #")
print ("#########################################################")
print ()
print ("Title of webpage: ", soup.title.text)

#Print meta data description
print ()
print ("#########################################################")
print ("# The following information is collected from meta data #")
print ("#########################################################")
print ()
meta = soup.find_all('meta')
for tag in meta:
	if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
		print ('Name    :',tag.attrs['name'].lower())
		print ('Content :',tag.attrs['content'])


#Print all comments in the source code
print ()
print ("########################################################")
print ("# The following comments are extracted from the source #")
print ("########################################################")
print ()
print ("===========")
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    print (c)
    print ("===========")
    c.extract()

#Print the hyperlinks found on the webpage
print ()
print ("############################################################################")
print ("# The following information about hyperlinks are extracted from the source #")
print ("############################################################################")
print ()
print ("===========")
for link in soup.find_all("a"):
    print ("Inner Text: {}".format(link.text))
    print ("Title: {}".format(link.get("title")))
    print ("Href: {}".format(link.get("href")))
    print ("===========")


#Enable option below if all source code should be printed
#print (soup.prettify()) # print the parsed data of html
