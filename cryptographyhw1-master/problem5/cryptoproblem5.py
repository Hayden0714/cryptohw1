# Hayden Olmstead
# 2/2/2022
# Applied Cryptography CS 4920
#
# problem 5
# This program is designed to be a program for the Caesar cipher

# The program is written in Python and utilizes numpy as a library to
# work with matrices easier
#
# I first read in the text from the file, scrub away the non-letters,
# perform the shifts necessary to encrypt the file, and then print to an
# output file
#
#
# #the main logic of the program can be found below the functions
# each problem on the homework sheet is divided into individual answers#

def main():
    #the main logic for the program where I complete the actual problems

    #PROBLEM B
    #encrypt the text of the class input b file and output to the class output b file
    encrypt(classInputB, classOutputB)

    #PROBLEM C
    #decrypt the cipher text and print to a file
    decrypt(classInputC, classOutputC)

    #PROBLEM D
    #generate my own input file, then encrypt it, then decrypt it back to my original plaintext




#function for encrypting a file
def encrypt(InputFile, OutputFile):
    #run the filterFile method to get the plaintext
    plaintext = filterFile(InputFile)

    #get the key
    key = getKey(InputFile)

    #go through each character and shift by the key amount
    ciphertext = ''
    for x in plaintext:
        cipherx = chr((ord(x) + 2 - 97) % 26 + 97)
        ciphertext = ciphertext + cipherx
    
    #print the ciphertext to an output file
    with open(OutputFile) as file_object:
        file_object.write(ciphertext)
    
#function for decrypting the ciphertext
def decrypt(InputFile, OutputFile):
    #get the key of the file
    key = getKey(InputFile)

    #get the text from the file
    ciphertext = filterFile(InputFile)

    #go through each of the elements and shift back to the original text
    plaintext = ''
    for element in ciphertext:
        plainx = chr((ord(element) - key - 97) % 26 + 97)
        plaintext = plaintext + plainx
    
    #print the output to the output file
    with open(OutputFile, 'w') as file_object:
        file_object.write(plaintext)

#function for filtering out all of the bad stuff
def filterFile(filename):
     # read the infomration from the file into a list
    with open(filename) as file_object:
        lines = file_object.readlines()

    # scrub the content string to get rid of characters we wont use
    filteredplaintext = ''
    content = lines[1]
    for char in content:
        if((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
            filteredplaintext += char

    finalplaintext = filteredplaintext.lower()

    return finalplaintext



#function for returning the key of the text
def getKey(filename):
    with open(filename) as file_object:
        content = file_object.read()
    
    intKey = ord(content[0] - 97)

    return intKey



#file constants
classInputB = 'problem5/class_input_b.txt'
classInputC = 'problem5/class_input_c.txt'
classOutputB = 'problem5/class_output_b.txt'
classOutputC = 'problem5/class_output_c.txt'



main()