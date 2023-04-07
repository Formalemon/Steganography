import argparse
from PIL import Image
import numpy as np

def extract_message(image_file, output_file):
    # open image file and convert to numpy array
    img = np.array(Image.open(image_file))
    # get dimensions of image
    height, width, channels = img.shape

    # loop through each pixel and extract LSBs of RGB values to recover message
    binary_message = ''
    i, j, channel = 0, 0, 0
    message_length = None
    for _ in range(32 + 8 * height * width):
        if i == height or (i == height - 1 and j == width):
            break
        bit = img[i][j][channel] & 1
        if message_length is None:
            binary_message += str(bit)
            if len(binary_message) == 32:
                message_length = int(binary_message, 2)
                binary_message = ''
        else:
            binary_message += str(bit)
            if len(binary_message) == 8 * message_length:
                break
        channel += 1
        if channel == 3:
            channel = 0
            j += 1
            if j == width:
                j = 0
                i += 1

    # convert binary message to text
    message = ''
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))

    # save extracted message to file
    with open(output_file, 'w') as f:
        f.write(message)

    return message

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract message from image')
    parser.add_argument('image', type=str, help='image file')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='output file')
    args = parser.parse_args()

    message = extract_message(args.image, args.output)
    print(f"Extracted message: {message}")
