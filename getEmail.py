import requests
from bs4 import BeautifulSoup
import re

def displayEmail(url):
    url = url
    agent = {"User-Agent":"Mozilla/60.0"}
    req = requests.get(url, headers=agent, verify=False)
    mails = set()  
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{2,4}", req.text, re.I))
    mails.update(new_emails)
    mail = []
    print ("Email addresses found on the webpage")
    print ("**********************************")
    for i in mails:
        if i not in mail:
            print(i)
            mail.append(i)
    print ("**********************************\n")