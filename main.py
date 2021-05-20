from bs4 import BeautifulSoup
import requests
import sys
import json

site = sys.argv[1]
r = requests.get(site, headers={"User-agent":"RiversideRocks"})
soup = BeautifulSoup(r.text, 'html.parser') # removes warning
#print(soup.prettify())
title = soup.title.string
print(title)

for meta in soup.find_all('meta'):
    if str(meta.get("property")) == "None":
      print("Skipping meta tag as it is blank...")
    else:
      print(str(meta.get("content")) + " - " + str(meta.get("property")))

#print(soup.meta)
