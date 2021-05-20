from bs4 import BeautifulSoup
import requests
import sys
import json
import os

details = []
site = sys.argv[1]
r = requests.get(site, headers={"User-agent":"RiversideRocks"})
soup = BeautifulSoup(r.text, 'html.parser') # removes warning
title = soup.title.string

for meta in soup.find_all('meta'):
    if str(meta.get("property")) == "None":
      print("Skipping meta tag as it is blank...")
    elif str(meta.get("property")) != "og:description":
      print("Skipping meta tag as it is wrong")
    else:
      desc = str(meta.get("content"))

json = open("result.json")
details.append(site)
details.append(title)
details.append(desc)
json.write(json.dumps(details))
file.close()
#print(soup.meta)
