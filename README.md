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




