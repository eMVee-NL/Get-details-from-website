# Get details from website
This script is written to extract some parts of the source code of the target website. In the near future I will work on updates to identify some information from headers and responses. Any suggestions and cowork are appreciated.

At this moment the following information is collected
- robots.txt file
- HTTP response headers
- Metadata of the website
- Email addresses (which are not obfuscated)
- Hyperlinks
- Comments

## Install some requirements
Run: `pip3 install -r requirements.txt`

## Usage
Run in the terminal `python3 ITechnology.py -u http://www.website.com`

## To do list
- Working on HTTP responses to get important details in a kind of summery
- Maybe a phone number scraper
- Maybe a check for hyperlinks (working on an idea)
  - Absolute links
  - Internal links
  - Anchored links
