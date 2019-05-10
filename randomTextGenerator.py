#Import required liraries
from urllib.request import urlopen
import operator
import random
import re

#Get 2 dimensional dictionary of text content
def getWordDict(content):
    content = re.sub("\n+", " ", content)
    content = re.sub("\"", "", content)

    punctuations = [',', '.', ';', ':', '?']    #string.punctuation - for more uncanny results
    for letter in punctuations:
        if letter in content:
            content = content.replace(letter, " "+letter+" ")

    splitcontent = content.split()
    wordDict = {}
    for i in range(1, len(splitcontent)):
        if splitcontent[i-1] not in wordDict:
            wordDict[splitcontent[i-1]] = {}
        if splitcontent[i] not in wordDict[splitcontent[i-1]]:
            wordDict[splitcontent[i-1]][splitcontent[i]] = 0

        wordDict[splitcontent[i-1]][splitcontent[i]] += 1

    return wordDict

#Get frequency of word from its word dictionary
def frequency(worddict):
    total = 0
    for key, value in worddict.items():
        total += value
    return total

#Get random word followed by a given word, from its word dictionary, using weighted value
def getRandomWord(worddict):
    totaloccurrence = frequency(worddict)
    randvalue = random.randint(1, totaloccurrence)
    for key, value in worddict.items():
        randvalue -= value
        if randvalue<=0:
            return key

#Main script
speech = urlopen("http://textfiles.com/apple/alinto.txt").read().decode("utf-8")
wordDict = getWordDict(speech)
#print(wordDict)

sentencelimit = 100
sentence = ""
word = "MOST"

for i in range(sentencelimit):
    sentence += word + " "
    word = getRandomWord(dict(sorted(wordDict[word].items(), key=operator.itemgetter(1))))

print(sentence)

"""
This script generates a funny/illogical sentence for "An Introduction to Assembly Language Programming on the Apple II", as follows (without using string.punctuation):

MOST OF SOPHISTICATION AT WHICH YIELDS THE MINI-ASSEMBLER 3) ASSEMBLER SOURCE LISTING . FROM THERE ARE BUT SOME ASSEMBLER IS THE FACT THAT YOU MAY DEVELOP A TIME AVOIDING A MACHINE LANGUAGE USING THE BSAVE COMMAND : *300G <RET> (TO MAKE IT INTO THE STARTING ADDRESS IN THIS IS INCLUDED IN AN ASSEMBLER . THERE , ENTER : SPEED , YOU ON A PUBLIC DOMAIN DISASSEMBLER IS NECESSARY TO THE LINE . . ENTERING INTEGER WITH THE '*' PROMPT . THEN 9 SETS OF MONEY TO HAVE A PROGRAM IN DECIMAL TO PEOPLE WHO KNOWS A MACHINE LANGUAGE DISK WILL
"""
