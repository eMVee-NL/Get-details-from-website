import sys, os, time
from urllib.parse import urlparse
import http.client

def createCollectedDataDirectory():
    try:
        os.mkdir('Collected-Data')
    except FileExistsError:
        pass

def createProjectDirectory(url):
    try:
        createCollectedDataDirectory()
        time.sleep(1)
        os.chdir('Collected-Data')
        time.sleep(1)
        url = url
        url = (url.split('//www.')[1])
        os.mkdir(url)
        print("Collected data will be written to directory Collected-Data/" + url)
    except FileExistsError:
        pass
    except Exception:
        pass