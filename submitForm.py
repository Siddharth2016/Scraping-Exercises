#import required libraries
import requests

inputData = {"firstname":"Siddharth", "lastname":"Chandra"}
returntext = requests.post("http://pythonscraping.com/pages/files/processing.php",
                           data = inputData)
print(returntext.text)
