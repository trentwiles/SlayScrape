from bs4 import BeautifulSoup
import requests
import sys
import json
import os

details = []
os.system("rm -rf result-stdin.json && touch result-stdin.json")
for line in sys.stdin:
    site = line
    #print(site)
    #sys.exit()
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

    js = open("result.json", "w")
    details.append(site)
    details.append(title)
    details.append(desc)
    js.write(json.dumps(details))
    js.close()
#print(soup.meta)
