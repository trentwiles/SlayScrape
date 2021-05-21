from bs4 import BeautifulSoup
import requests
import sys
import json
import os

site = sys.argv[1] # original site to scrape is passed via args
r = requests.get(site, headers={"User-agent":"RiversideRocks"})

soup = BeautifulSoup(r.text, 'html.parser') # removes warning

for link in soup.find_all('a'):
    url = link.get('href')
    if url[0:4] != "http":
      scan = site + url
    else:
      scan = url
    print(scan)
