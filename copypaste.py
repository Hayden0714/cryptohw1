def getFilteredText(filename):
    # read the infomration from the file into a list
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()

    # scrub the content string to get rid of characters we wont use
    filteredplaintext = ''
    content = lines[1]
    for char in content:
        if((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
            filteredplaintext += char

    finalplaintext = filteredplaintext.lower()

    return finalplaintext






    
def getKey(filename):
    with open(filename) as file_object:
        content = file_object.read()

    intKey = ord(content[0]) - 97

    return intKey
# main logic of the program






def decrypt(ciphertext, s, filename):
    # go through each element and shift it by the amount specified in x
    plaintext = ''
    for element in ciphertext:

        plainx = chr((ord(element) - s - 97) % 26 + 97)

        plaintext = plaintext + plainx

    # print the output to an output file
    with open(filename, 'a') as file_object:
        file_object.write(plaintext)
        file_object.write("\n")





        def encrypt(plaintext, s, filename):
    # go through each element in the plaintext and convert it to the
    # character that is s amount of spaces down
    ciphertext = ''
    for x in plaintext:
        cipherx = chr((ord(x) + s - 97) % 26 + 97)

        ciphertext = ciphertext + cipherx

    # print the plaintext to an output file
    with open(filename, 'w') as file_object:
        file_object.write(ciphertext)