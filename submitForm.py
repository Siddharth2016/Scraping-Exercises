#import required libraries
import requests

inputData = {"firstname":"Siddharth", "lastname":"Chandra"}
returnText = requests.post("http://pythonscraping.com/pages/files/processing.php",
                           data = inputData)
print(returnText.text)
