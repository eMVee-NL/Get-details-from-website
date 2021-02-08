import requests
from bs4 import BeautifulSoup
from bs4 import Comment

#Print the hyperlinks found on the webpage
def displayComments(url):
    # Make a GET request to fetch the raw HTML content
    agent = {"User-Agent":"Mozilla/60.0"}
    html_content = requests.get(url, headers=agent).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    print ("Comments found in the source code")
    print ("**********************************")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        print (c)
        print ("================================")
        c.extract()
    print ("**********************************\n")