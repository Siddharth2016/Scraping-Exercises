from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import datetime
import random
import json
import re

random.seed(datetime.datetime.now())

def getCountry(ipaddr):
    responseString = urlopen("http://api.ipstack.com/"+ipaddr+"?access_key=db42b142218bddc287a5eaaef13deebc").read().decode("utf-8")
    responseJson = json.loads(responseString)
    return responseJson.get("country_name")

def getLinks(url):
    html = urlopen("http://www.wikipedia.org/"+url)
    bsObj = bs(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                                                           href=re.compile("^(/wiki/)((?!:).)*$"))

def getIP(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"

    html = urlopen(historyUrl)
    bsObj = bs(html, "lxml")
    #finds only the links with class "mw-anonuserlink" which has IP addresses
    #instead of usernames
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")
while(len(links) > 0):
    for link in links:
        print("-------------------")
        historyIPs = getIP(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP, getCountry(historyIP))
    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
