# Get details from website
This script is written to extract some parts of the source code of the target website. In the near future I will work on updates to identify some information from headers and responses. Any suggestions and cowork are appreciated.

The collected data can be found in the directory: "Collected-data/website"
For each website a working directory will be created.

At this moment the following information is collected
- IP address belonging to the website (domain)
- robots.txt file
- Create a screenshot of the webpage
- HTTP response headers
- Metadata of the website
- Email addresses (which are not obfuscated)
- Hyperlinks
- Comments


## Install some requirements
Run: `pip3 install -r requirements.txt`    
   To succesfully take screenshot of a webpage the following should be performed. Be aware that during the copy  action the sudo password is asked. 
PS. don't trust any script and check the script before editing and using. :smile:   
Execture: `chmod +x install-GeckoDriver.sh`   
Run: `./install-GeckoDriver.sh`   

## Usage
Run in the terminal `python3 ITechnology.py -u http://www.website.com`

## To do list
- Working on the -l (list in a file) option to run multiple wwebsites (sub)domains
- Working on HTTP responses to get important details in a kind of summery
- Maybe a phone number scraper
- Maybe a check for hyperlinks (working on an idea)
  - Absolute links
  - Internal links
  - Anchored links
