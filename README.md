# Image Cryptography

## Overview
This project implements a steganography system that allows users to:

- Encrypt messages using XOR, Caesar, or Vigenère ciphers

- Hide encrypted messages within image files using LSB (Least Significant Bit) steganography

- Extract and decrypt hidden messages from images

- Compare original and modified images to detect changes

## Features
### Algorithms used
- XOR cipher
- Caesar cipher
- Vigenère cipher

### Image Processing
- Works with both grayscale and RGB images

### Message Handling
- Start/end sequence markers for message identification
- Binary conversion utilities
- Bit offset support for flexible message placement

## Example Test Cases
### Encryption
XOR Cipher
- <img width="722" height="333" alt="Screenshot 2025-08-13 144007" src="https://github.com/user-attachments/assets/4026a8a2-3689-4079-9f16-4d738ab1a32d" />

Caesar Cipher
- <img width="716" height="327" alt="Screenshot 2025-08-13 144211" src="https://github.com/user-attachments/assets/8b76cfeb-7af7-4db7-b817-0081ac2e7689" />

Vigenère cipher
- <img width="706" height="320" alt="image" src="https://github.com/user-attachments/assets/af3924a4-c781-4fbf-976a-e6251d10ba5b" />

### Decryption
XOR Cipher
- Original Image


  <img width="100" height="100" alt="ref_gry_x" src="https://github.com/user-attachments/assets/485bb4bc-7220-4e5f-9b43-0b954b40eae8" />
- <img width="747" height="260" alt="Screenshot 2025-08-14 094213" src="https://github.com/user-attachments/assets/f1fa376a-a373-4869-a175-bbf5a829d946" />


Caesar Cipher
- Original Image

  
  <img width="100" height="100" alt="ref_gry_c" src="https://github.com/user-attachments/assets/20f8cb2a-1c34-4bf2-a292-9fb2e0e8c7a0" />
- <img width="955" height="266" alt="image" src="https://github.com/user-attachments/assets/e30e9b74-114a-4075-a562-c4040bac734e" />


Vigenère cipher
- Original Image


  <img width="100" height="100" alt="ref_col_v" src="https://github.com/user-attachments/assets/7a161b37-31ec-4498-9628-863ea0c8fc37" />
- <img width="956" height="277" alt="image" src="https://github.com/user-attachments/assets/609f7fdb-895b-45cc-8a8e-6c1db72976a9" />
