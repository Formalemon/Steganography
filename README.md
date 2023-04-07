# Steganography Application
This is a steganography application that allows you to hide text in an image as well as extract the text from the image. It uses the LSB (Least Significant Bit) method to hide the text in the image.
- It is written in Python and uses the Pillow library to manipulate the image pixels, while the GUI is created using the Tkinter library.

## Installation
Clone the repository and navigate to the directory.
```bash
git clone https://github.com/Formalemon/Steganography
cd Steganography
```
### _Optional:_ Create a virtual environment for the project. ***(Recommended)***

In the terminal, run the following command to create a virtual environment for the project:
```bash
python -m venv .venv
```
or through the command palette in VS Code by following these steps:
1. Press `Ctrl+Shift+P` or `Cmd+Shift+P` to open the command palette.
2. Type `Python: Create Environment` and select the option.
3. Select `venv` as the environment type.
4. Select the `desired interpreter` or `Python version`.

reference: https://code.visualstudio.com/docs/python/environments

- - - - 

Next install the Pillow library and numpy, run the following command:
```bash
pip install pillow numpy
```


## Usage
### Running the GUI application.
To run the application, run the following command:
```bash
python main.py
```
Few things to note *(please read before using the GUI)*:
- When hiding the text in the image, all the fields are required. 
    - The Input file is the image file that you want to hide the text in. 
    - The Output file is the name of the image file that will be created after the text is hidden in the image.
    - The Message is the text that you want to hide in the image. The Message file is the text file that contains the text that you want to hide in the image. If you want to hide the text from a text file, then you can select the Message file option and select the text file.
- When extracting the text from the image, only the Input file is required and output field is required.
    - The Input file is the image file that you want to extract the text from.
    - The Output file is the name of the text file that will be created after the text is extracted from the image.
    > **Note:** Name the output file with the `.txt` extension and select the `All Files` option in the file dialog box.
    

### Running the hide_message.py and extract_message.py files individually.
To run the application which hides the text in the image, run the following command:
```bash
python hide_message.py <image_file> (-m MESSAGE | -f MESSAGE_FILE) [output_file]
```

To run the application that extracts the text from the image, run the following command:
```bash
python extract_message.py <image_file> [output_file_txt]
```

## TODO _(in priority order)_
- [ ] Dark mode.
- [ ] Simpler and more user-friendly GUI.
- [ ] Better error handling.
- [ ] Simpler documentation.
- [ ] Make a standalone executable file.
- [ ] Add more steganography methods.
