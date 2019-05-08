from urllib.request import urlopen
from io import StringIO
import csv

csvdata = urlopen("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv").read().decode("ascii", "ignore")
csvdatafile = StringIO(csvdata)
csvreader = csv.reader(csvdatafile)

for row in csvreader:
    print(row)
