from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLinks(url):
    
    html = urlopen("http://en.wikipedia.org"+url)
    bsObj = BS(html, "html.parser")
    return bsObj.find("div",
                      {"id":"bodyContent"}).findAll("a",
                                                    href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")

while(len(links)>0):
    newarticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newarticle)
    links = getLinks(newarticle)

"""print(len(bsObj.findAll("div", {"id":"bodyContent"})))

print(len(bsObj.find("div", {"id":"bodyContent"})))
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                                                               href=re.compile("^(/wiki/)((?!:).)*$")):
    #print(link)
    if "href" in link.attrs:
        print(link.attrs["href"])
"""
