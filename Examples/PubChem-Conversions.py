## Imports module to make basic arrays and module to grab text from url's
import array
import urllib.request

## Sets the input chemical name to be global. Can be called from any function.
def firstChoice():
    global string2
    string2 = input("Enter a chemical name: ")

## Multi Function to print some formatting to whats being requested by user.
## Also takes user input and the sets the input as a global variable.
def choices():
    print(40 * "_")
    print(3 * " " + "Select the value below to retrieve")
    print(40 * "_")
    print('{:>23}'.format("INCHI[0]"))
    print('{:>23}'.format("INCHIKEY[1]"))
    print('{:>23}'.format("MOLECULAR FORMULA[2]"))
    print('{:>23}'.format("SMILES[3]"))
    print('{:>23}'.format("MOLECULAR WEIGHT[4]"))
    print(40 * "_")
    global idChoice
    idChoice = int(input("Enter a number choice? "))
    if 0 <= idChoice <= 4:
        choiceID()
    elif idChoice != range(0,4):
        print(2 * '\n' + 38 * '*')
        print("* Incorrect Number Choice, Try Again *")
        print(38 * '*' + 2 * '\n')
        choices()

## Takes the possible inputs available, matches it to array list of what user
## selected in previous function and then performs a REST web request and prints
## the return string from the request.
def choiceID():
    inputList = ['INCHI', 'INCHIKEY', 'MolecularFormula','CanonicalSMILES', 'MolecularWeight']
    selChoice = inputList[idChoice]

    string1 = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
    string3 = "/property/" 
    string4 = "/TXT"
    html = urllib.request.urlopen(string1 + string2 + string3 + selChoice + string4).read()
    html2 = html.decode('UTF-8')
    print(2 * '\n')
    print(html2)
    print(2 * '\n')
    redoProg = input("Would you like to check another compound, yes or no? ")
    if redoProg == "yes":
        print ("\n" * 2)
        main()
    else:
        print("Done!")

## Main function that defines the order and chaos of the rest of the program.
def main():
    firstChoice()
    choices()

## Program Assignments ##
main()
