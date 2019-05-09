#Import Required Libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from collections import Counter
import string
import re

#Function to clean the input text string
def cleanInput(inp):
    inp = re.sub("\n+", " ", inp)
    inp = re.sub("\[[0-9]*\]", "", inp)
    inp = re.sub(" +", " ", inp)
    inp = bytes(inp, "utf-8")
    inp = inp.decode("ascii", "ignore")
    inp = inp.split()
    cleanedInput = []
    for text in inp:
        text = text.strip(string.punctuation)
        if len(text)>1:
            cleanedInput.append(text.lower())   #Lower case to further eliminate similar text
    return cleanedInput

#Computing N-Grams of the given text string
def nGrams(content, n):
    content = cleanInput(content)
    output = []
    for i in range(len(content)-n+1):
        output.append(str(content[i:i+n]))
    return Counter(output)  #Getting frequency of unique bigrams

#Main script
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BS(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
bigrams = nGrams(content, 2)
trigrams = nGrams(content, 3)
#print(bigrams)
print("Total Unique Bigrams", len(bigrams.items()), "Total Bigrams", sum(bigrams.values()))
print("Total Unique Trigrams", len(trigrams.items()), "Total Trigrams", sum(trigrams.values()))

"""
So as the value of 'n' increases to a certain limit, the unique ngrams increases, making it difficult to find patterns in text.
"""
