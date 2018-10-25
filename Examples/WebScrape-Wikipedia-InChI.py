from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

chemical = input("Put in the name of the chemical you want the InChI for: ")

html = urlopen("https://en.wikipedia.org/wiki/" + chemical)
wikiExtract = BeautifulSoup(html, "lxml").get_text()

inchiMatch = re.findall("InChI=.*", wikiExtract)
inchiClean = inchiMatch[0].split('H\\')
inchiFinal = inchiClean[0].split()

print("\n" + "Wikipedia says the InChI is:" + '\n')
print(inchiFinal[0])
