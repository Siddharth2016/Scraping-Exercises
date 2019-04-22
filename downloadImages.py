#Import required libraries
from urllib.request import urlretrieve, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS
import argparse
import time
import os

#To measure the execution time of script
start_time = time.time()

def ExtractImageTag(obj):
    """
    Function to extract and return all image tags present in a BeautifulSoup object
    """
    taglist = obj.findAll("img")
    return taglist

def ExtractTagSrc(taglist):
    """
    Function to extract source tag from the given tag if present
    """
    srclist = []
    for tag in taglist:
        if "src" in tag.attrs:
            srclist.append(tag.attrs["src"])
    return srclist

def GenerateImageURL(site, src):
    """
    Function to validate whether src tag contain an image or not
    """
    if "http://" in src[:11] or "www." in src[:11] or "https://" in src[:11]:
        return src
    try:
        url = urlopen(site+src)
        if url is not None:
            return site+src
    except:
        return None
    
#Making argument parser for CLI
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

#Making our Soup object for given website
html = urlopen(args["website"])
bsObj = BS(html, "html.parser")
tags = ExtractImageTag(bsObj)
#print(tags)
tagsources = ExtractTagSrc(tags)

#Downloading source images that are available
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

#Total time of execution
print("Execution Time", time.time()-start_time)
