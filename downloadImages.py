#Import Required Libraries
from urllib.request import urlretrieve, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS
import argparse
import time
import os

start_time = time.time()

def ExtractImageTag(obj):
    taglist = obj.findAll("img")
    return taglist

def ExtractTagSrc(taglist):
    srclist = []
    for tag in taglist:
        if "src" in tag.attrs:
            srclist.append(tag.attrs["src"])
    return srclist

def GenerateImageURL(site, src):
    if "http://" in src[:11] or "www." in src[:11] or "https://" in src[:11]:
        return src
    try:
        url = urlopen(site+src)
        if url is not None:
            return site+src
    except:
        return None
    

parser = argparse.ArgumentParser()
parser.add_argument("--website", help="Input website link for extracting images")
parser.add_argument("--dirname", help="Input directory to save images")
args = vars(parser.parse_args())

dirname = args["dirname"]
if dirname[0]=="/":
    dirname = dirname[1:]
if dirname[-1]=="/":
    dirname = dirname[:-1]
if not os.path.exists(dirname):
    os.mkdir(dirname)
    
html = urlopen(args["website"])
bsObj = BS(html, "html.parser")
tags = ExtractImageTag(bsObj)
#print(tags)
tagsources = ExtractTagSrc(tags)

for src in tagsources:
    imgurl = GenerateImageURL(args["website"], src)
    #print(imgurl)
    if imgurl is not None:
        imgname = src.split('/')[-1]
        try:
            urlretrieve(imgurl, dirname+"/"+imgname)
            print("Image",imgname,"saved in", dirname)
        except HTTPError:
            print(imgurl, "doesn't exist")

print("Execution Time", time.time()-start_time)
