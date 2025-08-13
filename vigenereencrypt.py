
import numpy as np
from matplotlib import pyplot as plt

def vigenere_encrypt(plaintext, key):
    #initialize the text to add to later
    ciphertext = []
    #initialize key length 
    key_length = len(key)
    #iterate over the characters in the plaintext
    for i, char in enumerate(plaintext):
        #create a baseline shift factor for the cipher
        shift = ord(key[i % key_length].upper()) - ord('A')
        if char.isalpha():  # Encrypt alphabetic characters
            #encrypt uppercase letters using the intialized shift factor
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            #encrypt lowercase letters using the same format as uppercase but change alphabet values
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            #add the ciphered characters to the initialized text
            ciphertext.append(encrypted_char)
        
        elif char.isdigit():  # Encrypt numeric characters
            encrypted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            #add ciphered numbers to cipher text
            ciphertext.append(encrypted_char)
        
        else:
            ciphertext.append(char)  # Non-alphanumeric characters remain unchanged
    
    return ''.join(ciphertext)

def text_to_bin(text):
    binary_list = [] # list to store all binary characters
    
    # Iterate through each character in the string
    for char in text:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
         
    # Join the binary values in the list and return as a single string
    return ' '.join(binary_list)



def main():
    #user input values
    plaintext = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for Vigenere cipher: ")
    startseq = input("Enter the start sequence: ")
    endseq = input("Enter the end sequence: ")
    #call the vigenere function from above
    encryptedmessage = vigenere_encrypt(plaintext, key)
    print(f"Encrypted Message using Vigenere Cipher: {encryptedmessage}")
    #create the binary message that will be displayed to the user
    binmess = startseq + encryptedmessage + endseq
    print(f"Binary output message: {text_to_bin(binmess)}")

if __name__ == "__main__":
    main()
