from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from urllib.parse import urlparse
from time import sleep

def takeScreenshot(url):
    domain = (url.split('//www.')[1])
    filename = "screenshot - " + domain + ".png"
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    sleep(1)
    driver.get_screenshot_as_file(domain + "/" + filename)
    print ("Screenshot")
    print ("**********************************")
    print ("Took a screenshot of the webpage: " + url)
    print ("Saved the file to: Collected-Data/" + domain + "/" + filename)
    print ("**********************************\n")

takeScreenshot('https://www.bartosz.nl')