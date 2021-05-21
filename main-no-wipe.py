from bs4 import BeautifulSoup
import requests
import sys
import json
import os

"""

Please note that to run this script you will need to
have a blank file called "result.json" ready to go in
the working directory

"""

details = []
#os.system("rm -rf result.json && touch result.json")
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

js = open("result.json", "a")
details.append(site)
details.append(title)
details.append(desc)
js.write(json.dumps(details))
js.write("\n")
js.close()
#print(soup.meta)
