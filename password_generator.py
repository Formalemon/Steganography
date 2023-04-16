import argparse
import string
import random

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ''.join([string.ascii_uppercase if include_uppercase else '',
                      string.ascii_lowercase if include_lowercase else '',
                      string.digits if include_digits else '',
                      string.punctuation if include_special else ''])

    password = ''.join(random.choices(characters, k=length))

    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a password with specified length and characters')
    parser.add_argument('length', type=int, help='the length of the password to generate')
    parser.add_argument('-lc', '--lowercase', action='store_false', help='exclude lowercase letters from the password')
    parser.add_argument('-uc', '--uppercase', action='store_false', help='exclude uppercase letters from the password')
    parser.add_argument('-n', '--numbers', action='store_false', help='exclude numbers from the password')
    parser.add_argument('-s', '--special', action='store_false', help='exclude special characters from the password')

    args = parser.parse_args()

    if args.length < 1:
        print('Password length must be at least 1')
        exit(1)
    password = generate_password(length=args.length, include_lowercase=args.lowercase, include_uppercase=args.uppercase, 
                                 include_digits=args.numbers, include_special=args.special)
    print(password)
    