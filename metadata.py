import requests
from bs4 import BeautifulSoup

#Print the meta data found on the webpage
def displayMetaData(url):
    # Make a GET request to fetch the raw HTML content
    agent = {"User-Agent":"Mozilla/60.0"}
    html_content = requests.get(url, headers=agent).text
    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    print ("Title of the website")
    print ("**********************************")
    try:
        print ("Title of webpage: ", soup.title.text)
    except:
        print ("An exception occurred, the title cannot be found!")
    print ("**********************************\n")
    print ("Meta data from the website")
    print ("**********************************")
    meta = soup.find_all('meta')
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords', 'generator']:
            print ('Name    :',tag.attrs['name'].lower())
            print ('Content :',tag.attrs['content'])
    print ("**********************************\n")


