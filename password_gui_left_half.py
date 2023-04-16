import tkinter as tk
from ttkbootstrap import ttk
from tkinter import messagebox
import password_generator
import datetime
import sqlite3
import password_gui_right_half

class PassGenLeftHalf(tk.Frame):
    def __init__(self, master=None, right_half=password_gui_right_half.PassGenRightHalf):
        super().__init__(master)
        self.right_half = right_half
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # set up database connection
        self.conn = sqlite3.connect('passwords.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT NOT NULL,
                                 password TEXT NOT NULL)''')

        # Password Length
        length_frame = ttk.Frame(self, padding="10 10 10 10")
        length_frame.pack(fill=tk.X)
        ttk.Label(length_frame, text="Password Length: ").pack(side=tk.LEFT)
        self.length_var = tk.StringVar(value="16")
        length_entry = ttk.Entry(length_frame, textvariable=self.length_var)
        length_entry.pack(side=tk.LEFT)

        # Include Uppercase
        self.uppercase_var = tk.BooleanVar(value=True)
        uppercase_check = ttk.Checkbutton(self, text="Include Uppercase", variable=self.uppercase_var)
        uppercase_check.pack(fill=tk.X, padx=10, pady=5)

        # Include Lowercase
        self.lowercase_var = tk.BooleanVar(value=True)
        lowercase_check = ttk.Checkbutton(self, text="Include Lowercase", variable=self.lowercase_var)
        lowercase_check.pack(fill=tk.X, padx=10, pady=5)

        # Include Numbers
        self.numbers_var = tk.BooleanVar(value=True)
        numbers_check = ttk.Checkbutton(self, text="Include Numbers", variable=self.numbers_var)
        numbers_check.pack(fill=tk.X, padx=10, pady=5)

        # Include Special Characters
        self.special_var = tk.BooleanVar(value=True)
        special_check = ttk.Checkbutton(self, text="Include Special Characters", variable=self.special_var)
        special_check.pack(fill=tk.X, padx=10, pady=5)

        # Generate Password Button
        generate_button = ttk.Button(self, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        # Password Textbox
        password_frame = ttk.Frame(self, padding="10 10 10 10")
        password_frame.pack(fill=tk.X)
        ttk.Label(password_frame, text="Generated Password: ").pack(side=tk.LEFT)
        self.password_var = tk.StringVar(value="")
        password_entry = ttk.Entry(password_frame, textvariable=self.password_var, state="readonly")
        password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Copy Password Button
        copy_button = ttk.Button(self, text="Copy to Clipboard", command=self.copy_password)
        copy_button.pack(pady=10)

    def generate_password(self):
        length = int(self.length_var.get())
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_numbers = self.numbers_var.get()
        include_special = self.special_var.get()

        if not (include_uppercase or include_lowercase or include_numbers or include_special):
            messagebox.showerror("Error", "At least one character type must be selected")
            return

        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1")
            return

        password = password_generator.generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)
        self.password_var.set(password)

    def copy_password(self):
        password = self.password_var.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password_var.get())

        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        self.cursor.execute("INSERT INTO passwords (name, password) VALUES (?, ?)", (date_time, password))
        self.conn.commit()
        self.right_half.load_passwords()