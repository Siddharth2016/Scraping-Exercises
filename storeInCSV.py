from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import csv

html = urlopen("https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar")
bsObj = BS(html, "html.parser")
table_of_interest = bsObj.findAll("table", {"class":"wikitable"})[1] # 1 for Test Centuries
rows = table_of_interest.findAll("tr")

csvFile = open("testCentury.csv", "w+")
writer = csv.writer(csvFile)

try:
    for row in rows:
        rowdata = []
        columns = row.findAll(["td", "th"])
        for col in columns:
            rowdata.append(col.get_text())
        writer.writerow(tuple(rowdata))
        print("Done with current row...")
finally:
    csvFile.close()
