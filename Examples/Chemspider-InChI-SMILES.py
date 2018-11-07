##ChemSpiPy is an excellent Python module developed to help make web requests
##to chemspider smooth and easy

from chemspipy import ChemSpider

##getpass allows discrete password or token input, however it is not called in
##this example. I will configure it later.
import getpass

##This token input is required to use the chemspider API.
token = input('Insert your API Token Here: ')

##assigns cs to use chemspipy format of the input token along with ChemSpider
##in the actual request. This format must use cs and ChemSpider based on the
##module being imported.
cs = ChemSpider(token)

##This takes the input string. Insert the entire string including the InChI=1S
##portion.
inchi = input("insert your inchi here: ")

##Most of the formatting here is for aesthetics purposes of how the results
##are displayed in the shell.
print("\n" + "Your SMILE STRING IS:\n" + 30*'-' + 10*" ")

##The conversion takes place here in which the cs.convert takes the 3 values
##in parenthesis as parameters and submits them to the chemspider web service
#which returns a SMILES string.
for result in cs.convert(inchi, 'InChI', 'SMILES'):
   print(result, end = '')
