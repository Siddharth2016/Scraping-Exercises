from urllib.request import urlopen
from io import StringIO
import csv

csvData = urlopen("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv").read().decode("ascii", "ignore")
csvDatafile = StringIO(csvdata)
csvReader = csv.reader(csvdatafile)

for row in csvReader:
    print(row)
