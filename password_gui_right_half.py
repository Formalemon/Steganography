import tkinter as tk
import ttkbootstrap as ttk
from tkinter import simpledialog
import sqlite3
from ttkbootstrap import Style, Button, Frame, Label

class Password:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PassGenRightHalf(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
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

        # set up GUI layout
        self.style = Style()
        self.style.theme_use('darkly')

        self.password_frame = Frame(self)
        self.password_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

        identifier_label = ttk.Label(self.password_frame, text="Your saved Passwords")
        identifier_label.pack(side=tk.TOP, padx=10, pady=10)

        self.password_canvas = tk.Canvas(self.password_frame)
        self.password_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.password_frame_inner = Frame(self.password_canvas)
        self.password_canvas.create_window((0,0), window=self.password_frame_inner, anchor='nw')

        self.password_frame_inner.bind("<Configure>", lambda e: self.password_canvas.configure(scrollregion=self.password_canvas.bbox("all")))
        self.password_canvas.bind_all("<MouseWheel>", lambda event: self.password_canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Set the width of the inner frame to be the width of the canvas minus 20 pixels of padding
        self.password_canvas.update()
        self.password_frame_inner.configure(width=self.password_canvas.winfo_width() - 20)

        self.load_passwords()
    
    def add_copied_password(self, name, value):
        if name and value:
            self.cursor.execute("INSERT INTO passwords (name, password) VALUES (?, ?)", (name, value))
            self.conn.commit()

    def load_passwords(self):
        # clear existing passwords
        for widget in self.password_frame_inner.winfo_children():
            widget.destroy()
    
        # load passwords from database
        self.cursor.execute("SELECT * FROM passwords ORDER BY id")
        rows = self.cursor.fetchall()
    
        # create password cards and add to frame
        num_rows = (len(rows) + 1) // 2  # calculate the number of rows needed
        for i in range(num_rows):
            password_card_row = Frame(self.password_frame_inner)
            password_card_row.pack(side=tk.TOP, pady=10, fill=tk.BOTH, expand=True)
    
            for j in range(2):
                index = i * 2 + j
                if index >= len(rows):
                    break
                
                row = rows[index]
                name = row[1]
                password = row[2]
                password_obj = Password(name, password)
    
                password_card = Frame(password_card_row, borderwidth=1, relief=tk.GROOVE, padding=10)
                password_name_label = Label(password_card, text=name, font='Arial 12 bold')
                password_name_label.grid(row=0, column=0, pady=5, columnspan=3)
                password_value_label = Label(password_card, text=password)
                password_value_label.grid(row=1, column=0, pady=5, columnspan=3)
                copy_button = Button(password_card, text='Copy', command=lambda obj=password_obj: self.master.clipboard_clear() or self.master.clipboard_append(obj.value))
                copy_button.grid(row=2, column=0, pady=5)
                edit_button = Button(password_card, text='Edit', command=lambda obj=password_obj: self.edit_password_name(obj))
                edit_button.grid(row=2, column=1, pady=5, padx=5)
                delete_button = Button(password_card, text='Delete', command=lambda obj=password_obj: self.delete_password(obj))
                delete_button.grid(row=2, column=2, pady=5)
                password_card.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
    
        # Set the width of the inner frame to be the width of the canvas minus 20 pixels of padding
        self.password_frame_inner.configure(width=self.password_canvas.winfo_width() - 20)
    
    def edit_password_name(self, password_obj):
        new_name = simpledialog.askstring("Edit Password", "Enter new name:", initialvalue=password_obj.name)
        if new_name:
            self.cursor.execute("UPDATE passwords SET name = ? WHERE password = ?", (new_name, password_obj.value))
            self.conn.commit()
            self.load_passwords()

    def delete_password(self, password_obj):
        self.cursor.execute("DELETE FROM passwords WHERE password = ?", (password_obj.value,))
        self.conn.commit()
        self.load_passwords()
