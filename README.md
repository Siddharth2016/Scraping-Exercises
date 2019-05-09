# Scraping-Exercises
This Repository features various web scraping exercises dealing in important concepts.

### downloadImages.py
This python3 script extracts images present on a website (provided the link). It deals with images present in HTML tag **img** and those that does not point to any other external image link, also if the link is not static it will be ignored. It uses agrparse library to handle CLI effectively.

### storeInCSV.py
It takes a website link, provided that website contains at least one table tag, then extract first table (can be modified as per need) and save it in CSV format on local hard drive.

### getCSVFile.py
This takes a CSV file remote link and helps to process it (file) in memory without actually being saved on local hard drive.

### wikiHistroyCountryName.py
This helps us to find the country of a user who made recent changes to a particular Wikipedia page. It uses ipstack API for finding the IP location of recent changes, which further helps to determine the country name.

### findNGrams.py
This script helps to find ngrams on a text obtained from python programming language wikipedia page.[Link](https://en.wikipedia.org/wiki/Python_(programming_language))
