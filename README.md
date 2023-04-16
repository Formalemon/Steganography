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
pip install pillow numpy ttkbootstrap
```


## Usage
### Running the GUI application.
To run the application, run the following command:
```bash
python main.py
```
Few things to note *(please read before using the GUI)*:
- In Hide Message:
    - The message can be either a text file or a string.
    - The password is optional, but if you want to use it, make sure to **remember** it.
    - Password defaults to `ididnotsetapassword` if not provided.
- In Extract Message:
    - The password is optional, but if you used it to hide the message, you **must** use it to extract the message.
    - The extracted message will be saved in a text file as well as displayed in the window.
    - You will get errors where the message is not extracted properly if you use a wrong password or if the image is not a steganographed image.
- In Password Generation:
    - You can generate a password of any length, but it is recommended to use a password of length 8 or more.
    - Use it to generate passwords for hiding messages.
    - The generated password will be displayed in the window as well as saved in a sqlite database.
    - The database is stored in the `passwords.db` file.
    - This is a very basic implementation of a password manager, so it is not recommended to use it for storing passwords for other purposes. [Very Basic Implementation with no safety features.]

    

### Running the hide_message.py, extract_message.py and password_generator.py files individually.
To run the application which hides the text in the image, run the following command:
```bash
python hide_message.py (image_file) (-m MESSAGE | -f MESSAGE_FILE) -p [password] -o [output_file]
```

To run the application that extracts the text from the image, run the following command:
```bash
python extract_message.py (image_file) -p [password] -o [output_file_txt]
```

To run the application that generates a password, run the following command:
```bash
python password_generator.py -h
```
> This will display the help message for the password generator. The usage and the arguments that can be passed to the application will be shown.

## TODO _(in priority order)_
- [x] Dark mode.
- [x] Simpler and more user-friendly GUI.
- [x] Better error handling.
- [x] Simpler documentation.
- [x] Make application switchable between light and dark mode.
- [x] Add a password generator and store it as well.
- [ ] Code optimization and less mess.
- [ ] Readable code.
- [ ] Add more comments.
- [ ] Make a secure password manager.
- [ ] Make a standalone executable file.
- ~~[ ] Add more steganography methods.~~ _i'm not sure if i want to do this_
