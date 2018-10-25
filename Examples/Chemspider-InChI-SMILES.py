from chemspipy import ChemSpider
import getpass

token = input('Insert your API Token Here: ')


cs = ChemSpider(token)

inchi = input("insert your inchi here: ")


print("\n" + "Your SMILE STRING IS:\n" + 30*'-' + 10*" ")

for result in cs.convert(inchi, 'InChI', 'SMILES'):
   print(result, end = '')