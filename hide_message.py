import argparse
from PIL import Image
import numpy as np
import hashlib

def encrypt_message(message, password):
    # hash the password to get a key
    hashed_password = hashlib.sha256(password.encode()).digest()
    # convert message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    # add null terminator to binary message
    binary_message += '00000000'
    # add message length to binary message
    binary_message = format(len(message), '032b') + binary_message
    # convert binary message to bytes
    message_bytes = bytearray()
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message_bytes.append(int(byte, 2))

    # xor message bytes with hashed password bytes
    encrypted_message = bytearray()
    for i in range(len(message_bytes)):
        encrypted_message.append(message_bytes[i] ^ hashed_password[i % len(hashed_password)])

    # convert encrypted message to binary
    encrypted_binary = ''.join(format(b, '08b') for b in encrypted_message)

    return encrypted_binary


def hide_message(image_file, message, message_file, password, output_file):
    # get message from file if specified
    if message is None and message_file is None:
        raise ValueError('Either message or message_file must be specified')
    
    if message is not None and message_file is not None:
        raise ValueError('Only one of message or message_file can be specified')
    
    if message is None:
        with open(message_file, 'r') as f:
            message = f.read()

    # open image file and convert to numpy array
    img = np.array(Image.open(image_file))
    # get dimensions of image
    height, width, channels = img.shape

    # encrypt message
    message = encrypt_message(message, password)

    # convert message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    # add null terminator to binary message
    binary_message += '00000000'

    # calculate number of pixels required to store message
    num_pixels_needed = len(binary_message) // 3 + int(len(binary_message) % 3 != 0)

    # check if message will fit in image
    if num_pixels_needed > height * width:
        print('Error: message is too large to fit in image')
        return

    # add message length to binary message
    binary_message = format(len(message), '032b') + binary_message

    # loop through each pixel and hide message in LSBs of RGB values
    i, j, channel = 0, 0, 0
    for bit in binary_message:
        if i == height or (i == height - 1 and j == width):
            break
        img[i][j][channel] = (img[i][j][channel] & ~1) | int(bit)
        channel += 1
        if channel == 3:
            channel = 0
            j += 1
            if j == width:
                j = 0
                i += 1

    # save modified image
    Image.fromarray(img).save(output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hide message onto image')
    parser.add_argument('image', type=str, help='the input image file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--message', type=str, help='the message to hide')
    group.add_argument('-f', '--message_file', type=str, help='the file containing the message to hide')
    parser.add_argument('-p', '--password', type=str, default='ididnotsetapassword', help='the password to encrypt the message with')
    parser.add_argument('-o', '--output', type=str, default='hidden.png', help='the output image file')
    args = parser.parse_args()

    hide_message(args.image, args.message, args.message_file, args.password, args.output)
    print(f"Message successfully hidden in {args.output}")