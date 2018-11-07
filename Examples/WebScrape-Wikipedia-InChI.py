## Imports modules to retrieve html text from url, Beautiful Soup helps to parse
## the html or xml. re helps with the expressions used. 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

## Regular variable input from the user.
chemical = input("Put in the name of the chemical you want the InChI for: ")

##Provides variables for the url syntax with user input
html = urlopen("https://en.wikipedia.org/wiki/" + chemical)

## Parses the information on page to easy to parse format.
wikiExtract = BeautifulSoup(html, "lxml").get_text()

##Performs Search operation, Extracts and formats the final requested output.
inchiMatch = re.findall("InChI=.*", wikiExtract)
inchiClean = inchiMatch[0].split('H\\')
inchiFinal = inchiClean[0].split()

##Prints the final variable.
print("\n" + "Wikipedia says the InChI is:" + '\n')
print(inchiFinal[0])