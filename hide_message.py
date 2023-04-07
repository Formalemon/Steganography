import argparse
from PIL import Image
import numpy as np

def hide_message(image_file, message, output_file):
    # open image file and convert to numpy array
    img = np.array(Image.open(image_file))
    # get dimensions of image
    height, width, channels = img.shape

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
    parser.add_argument('message', type=str, help='the message to hide')
    parser.add_argument('-o', '--output', type=str, default='hidden.png', help='the output image file')
    args = parser.parse_args()

    hide_message(args.image, args.message, args.output)
    print(f"Message successfully hidden in {args.output}")