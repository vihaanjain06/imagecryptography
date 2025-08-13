import numpy as np
from matplotlib import pyplot as plt
from uploadimage import upload_image

def text_to_bin(text):
    binary_representation = ''.join(format(ord(char), '08b') for char in text)
    return binary_representation

def decimal_to_bin(num):
    #if value = 0 turn into binary zero
    if num == 0:
        return '00000000'
    binary = []
    #everything but zero turn into binary
    while num > 0:
        binary.insert(0, str(num % 2))
        num = num // 2
    #creating the full binary sequence
    result = ''.join(binary)
    return result

def bin_to_string(binary):
    strdata = "" # string to store final message
    for i in range(0, len(binary), 8): # for every 8 characters in the binary string
        temp_data = binary[i:i + 8] # temporary variable to store current 8 characters being converted
        decimal_data = bin_to_decimal(temp_data) # function call to convert binary to ascii charcater

        strdata = strdata + chr(decimal_data) # adding string to character converted from ascii
    
    return strdata

def bin_to_decimal(binary):
    dec = int(binary,2) # converting 8 digit binary back to ascii using base 2
    return dec

def getExtractedSequence(startseq, endseq, image):
    startseq = text_to_bin(startseq) # convert start to binary
    endseq = text_to_bin(endseq) # convert end to binarys
    #convert each character into ascii value
    lsbs = ""
    #for colored images with three dimensions
    if(image.ndim == 3):
        for row in range(len(image)):
            for col in range(len(image[row])):
                for col2 in range(len(image[row, col])):
                    temp = decimal_to_bin(image[row][col][col2])
                    lsbs += temp[-1]
    #for grey images with two dimensions    
    if(image.ndim == 2):
        for row in range(len(image)):
            for col in range(len(image[row])):
                temp = decimal_to_bin(image[row][col])
                lsbs += temp[-1]
    #find the start and end in the binarys string
    
    start = lsbs.find(startseq)
    end = lsbs.find(endseq)
    #convert to int for extracting
    startint = int(start)
    endint = int(end)
    #error handling
    if(startint == -1 or endint == -1):
        print("Start or end sequence not found in the image.")
    #print binary message
    else:
        extract = lsbs[startint:endint]
        return extract
    
def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    key_int = [(ord(i.lower()) - 97) % 26 for i in key]  # Normalize key to 0-25, ignoring case

    for i, char in enumerate(ciphertext):
        if 'A' <= char <= 'Z':
            value = (ord(char) - 65 - key_int[i % key_length]) % 26
            plaintext.append(chr(value + 65))
        elif 'a' <= char <= 'z':
            value = (ord(char) - 97 - key_int[i % key_length]) % 26
            plaintext.append(chr(value + 97))
        elif '0' <= char <= '9':
            # Use the key value modulo 10 for numeric characters
            value = (ord(char) - 48 - (key_int[i % key_length] % 10)) % 10
            plaintext.append(chr(value + 48))
        else:
            plaintext.append(char)  # Leave unsupported characters unchanged

    return ''.join(plaintext)


def caesar_decrypt(ciphertext, key):
    plaintext = []
    
    for char in ciphertext:
        if char.isupper():  # Check if the character is an uppercase alphabet
            shift = (ord(char) - key - 65) % 26
            plaintext.append(chr(shift + 65))
        elif char.islower():  # Check if the character is a lowercase alphabet
            shift = (ord(char) - key - 97) % 26
            plaintext.append(chr(shift + 97))
        else:
            plaintext.append(char)  # Keep non-alphabet characters unchanged
    
    return ''.join(plaintext)

def xor_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i % key_length]))
        plaintext.append(decrypted_char)
    
    return ''.join(plaintext)

def main():
    #user input values
    cipher = input("Enter the cipher you want to use for encryption: ")
    key = input("Enter the key for the cipher: ")
    startseq = input("Enter the start sequence: ")
    endseq = input("Enter the end sequence: ")
    inputpath = input("Enter the path of the input image: ")
    #read the image and change its structure
    img = upload_image(inputpath)
    encryptedbinary = getExtractedSequence(startseq, endseq, img)
    print(f"Extracted Binary Message: {encryptedbinary}")
    convbin = str(bin_to_string(encryptedbinary))[len(startseq):]
    print(f"Converted Binary Text: {convbin}")
    if(cipher == "xor"):
        convertedtext = xor_decrypt(convbin, key)[:-1]
    elif(cipher == "vigenere"):
        convertedtext = vigenere_decrypt(convbin, key)
    elif(cipher == "caesar"):
        convertedtext = caesar_decrypt(convbin, int(key))
    print(f"Converted Text: {convertedtext}")
if __name__ == "__main__":
    main()


