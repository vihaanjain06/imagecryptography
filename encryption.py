import numpy as np
from matplotlib import pyplot as plt
import vigenereencrypt as t2
from PIL import Image

def xor_encrypt(plaintext, key):
    encrypted_chars = []
    key_length = len(key)
    
    for i in range(len(plaintext)):
        # XOR each character in the plaintext with the corresponding character in the key
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i % key_length])) 
        encrypted_chars.append(encrypted_char)
    
    # Join the encrypted characters into a single string
    encrypted_text = ''.join(encrypted_chars)
    return encrypted_text

def caesar_cipher(plaintext, shift):
    encrypted_text = []
    
    for char in plaintext:
        # Check if the character is an uppercase letter
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Check if the character is a digit
        elif char.isdigit():
            encrypted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_char = char
        
        encrypted_text.append(encrypted_char)
    
    # Join the encrypted characters into a single string
    return ''.join(encrypted_text)

def encode_binary_message(binary_message, input_image_path, output_image_path, bit_offset):
    # Remove any spaces and ensure the binary message contains only '0' and '1'
    binary_message = binary_message.replace(" ", "").strip()
    
    # Load the image
    img = plt.imread(input_image_path)
    
    # Convert float values (0-1) to integer values (0-255) for RGB images
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = (img * 255).astype(np.uint8)
    
    if img.ndim == 3:
        height, width, num_channels = img.shape
        total_bits = width * height * num_channels
    elif img.ndim == 2:
        height, width = img.shape
        total_bits = width * height
    else:
        print("Error: Unsupported image format.")
        return
    
    # Check if the binary message can fit into the image
    if len(binary_message) > total_bits - bit_offset:
        print("Error: The binary message is too long to fit into the image.")
        return

    # Grayscale image encoding
    if img.ndim == 2:
        index = bit_offset  # Start from the bit offset
        for i in range(height):
            for j in range(width):
                if index >= len(binary_message):
                    break
                
                pixel_value = img[i, j]

                # Binary representation of the pixel
                temp = format(pixel_value, '08b')

                # Modify the LSB
                temp2 = temp[:-1] + binary_message[index]
                new_pixel_value = int(temp2, 2)
                img[i,j] = new_pixel_value
                #current_pixel_value = img[i, j]
                # Remove the LSB of the pixel by setting it to 0
                #current_pixel_value = current_pixel_value - (current_pixel_value % 2)
                # Add the new LSB (which is either 0 or 1)
                #img[i, j] = current_pixel_value + (new_pixel_value % 2)
                index += 1
        plt.imshow(img, cmap="gray")
        plt.show()
        # Save the modified grayscale image using PIL
        pil_image = Image.fromarray(img, mode="L")
        pil_image.save(output_image_path)
    
    # RGB image encoding
    elif img.ndim == 3:
        img = img[:, :, :3]  # Only use RGB channels if there's an alpha channel
        index = bit_offset  # Start from the bit offset
        for i in range(height):
            for j in range(width):
                for k in range(num_channels - 1):
                    if index >= len(binary_message):
                        break
                    pixel_value = int(img[i, j, k])

                    # Binary representation of the pixel
                    temp = format(pixel_value, '08b')

                    # Modify the LSB
                    temp2 = temp[:-1] + binary_message[index]
                    new_pixel_value = int(temp2, 2)

                    current_pixel_value = img[i, j, k]
                    # Remove the LSB of the pixel by setting it to 0
                    current_pixel_value = current_pixel_value - (current_pixel_value % 2)
                    # Add the new LSB (which is either 0 or 1)
                    img[i, j, k] = current_pixel_value + (new_pixel_value % 2)
                    index += 1

        # Save and display the modified RGB image
        plt.imsave(output_image_path, img)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    
    print("Message encoded and image saved to:", output_image_path)

def compare_images(image1, image2):
    if image1.ndim != image2.ndim:
        print("Cannot compare images in different modes (RGBA and L).")
        return False
    same = True   # Initialize the images if true unless proven otherwise later in function
    #if the images aren't the same size tell user
    #if image1.shape != image2.shape:
     #   print("Not same size")
      #  return False
    #error handling for input of one grey and one color image
    if image1.ndim == 2 and image2.ndim == 3:
        print("Cannot compare images in different modes (RGBA and L).")
        same = False
    #same as above but for other way around
    elif image1.ndim == 3 and image2.ndim == 2:
        print("Cannot compare images in different modes (RGBA and L).")
        same = False
    #initialize an array for the different image that will be adjusted later on
    diffimage = np.zeros_like(image1)
    if image1.dtype == np.float32 or image1.dtype == np.float64:
        image1 = (image1 * 255).astype(np.uint8)
    if image2.dtype == np.float32 or image2.dtype == np.float64:
        image2 = (image2 * 255).astype(np.uint8)

    if image1.ndim == 2:  # Gray image
        for row in range(image1.shape[0]):  # Loop rows
            for col in range(image1.shape[1]):  # Loop columns
                #condition for the same pixel
                if image1[row, col] == image2[row, col]:
                    diffimage[row, col] = 0
                #condition for different pixel
                else:
                    diffimage[row, col] = 255
                    same = False  
        plt.imshow(diffimage, cmap="gray")
        plt.show()

    elif image1.ndim == 3:  # Color image
        for row in range(image1.shape[0]):  # Loop rows
            for col in range(image1.shape[1]):  # Loop columns
                for pixel in range(image1.shape[2] - 1):  # Loop color channels
                    #if pixel structure is the same
                    if round(image1[row, col, pixel], -1) == round(image2[row, col, pixel], -1):
                        diffimage[row, col, pixel] = 0
                    #if pixel structure is different
                    else:
                        diffimage[row, col, pixel] = 255
                        same = False  
    #if the image is in four dimensions instead of 3 change it to three
    if image1.ndim == 3:
        diffimage = diffimage[..., :3]
        plt.imshow(diffimage)
        plt.show()

    #show the image and return the same boolean
    
    return same


def main():
    cipher = input("Enter the cipher you want to use for encryption: ")
    plaintext = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for the cipher: ")
    startseq = input("Enter the start sequence: ")
    endseq = input("Enter the end sequence: ")
    bitoffset = input("Enter the bit offset before you want to start encoding: ")
    inputpath = input("Enter the path of the input image: ")
    encodedpath = input("Enter the path for your encoded image: ")
    comparepath = input("Enter the path of the image you want to compare: ")

    
    if cipher == "xor":
        encryptedmessage = xor_encrypt(plaintext, key)
        print(f"Encrypted Message using XOR Cipher: {encryptedmessage}")
    elif cipher == "caesar":
        encryptedmessage = caesar_cipher(plaintext, int(key))
        print(f"Encrypted Message using caesar Cipher: {encryptedmessage}")
    elif cipher == "vigenere":
        encryptedmessage = t2.vigenere_encrypt(plaintext, key)
        print(f"Encrypted Message using vigenere Cipher: {encryptedmessage}")

    binmessage = t2.text_to_bin(startseq + encryptedmessage + endseq)
    print(f"Binary output message: {binmessage}")
    encode_binary_message(binmessage, inputpath, encodedpath, int(bitoffset))
    image1 = plt.imread(encodedpath)
    image2 = plt.imread(comparepath)
    image1 = image1 * 255
    image2 = image2 * 255
    same = compare_images(image1, image2)

    if same:
        print("Images are same")
    else:
        print("Images are the different.")
    

    
if __name__ == "__main__":
    main()


