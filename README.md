# Steganography Application
This is a steganography application that allows you to hide text in an image. 
It is written in Python 3.6.5 and uses the Pillow library.

## Installation
Clone the repository and navigate to the directory.
```bash
git clone https://github.com/Formalemon/Steganography
cd Steganography
```
### Optional: Create a virtual environment for the project.
Creating a virtual environment in VS Code, run the following command:
```bash
python -m venv .venv
```
or through the command palette in VS Code by following these steps:
1. Press `Ctrl+Shift+P` or `Cmd+Shift+P` to open the command palette.
2. Type `Python: Create Environment` and select the option.
3. Select `venv` as the environment type.
4. Select the `desired interpreter or Python version`.

reference: https://code.visualstudio.com/docs/python/environments
#

Next install the Pillow library, run the following command:
```bash
pip install Pillow
```

#
## Usage
To run the application which hides the text in the image, run the following command:
```bash
python hide_message.py <image_file> (-m MESSAGE | -f MESSAGE_FILE) [output_file]
```

To run the application that extracts the text from the image, run the following command:
```bash
python extract_message.py <image_file> [output_file_txt]
```