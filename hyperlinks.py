import requests
from bs4 import BeautifulSoup

#Print the hyperlinks found on the webpage
def displayHyperlinks(url):
    # Make a GET request to fetch the raw HTML content
    agent = {"User-Agent":"Mozilla/60.0"}
    html_content = requests.get(url, headers=agent).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    print ("Hyperlinks found on the webpage")
    print ("**********************************")
    for link in soup.find_all("a"):
        print ("Inner Text: {}".format(link.text))
        print ("Title: {}".format(link.get("title")))
        print ("Href: {}".format(link.get("href")))
        print ("================================")
    print ("**********************************\n")
