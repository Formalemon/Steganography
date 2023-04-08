import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
from extract_message import extract_message

class ExtractGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Input file
        input_frame = ttk.Frame(self)
        input_frame.pack(fill="x", padx=10, pady=5)
        input_label = ttk.Label(input_frame, text="Input file:")
        input_label.pack(side="left", padx=5)
        input_entry = ttk.Entry(input_frame, state="readonly")
        input_entry.pack(side="left", fill="x", expand=True, padx=5)
        input_button = ttk.Button(input_frame, text="Browse...", command=self.get_input_file)
        input_button.pack(side="left", padx=5)
        self.input_entry = input_entry

        # Password frame and entry
        password_frame = ttk.Frame(self)
        password_frame.pack(fill="x", padx=10, pady=5)
        password_label = ttk.Label(password_frame, text="Password:")
        password_label.pack(side="left", padx=5)
        password_entry = ttk.Entry(password_frame, show="*")
        password_entry.pack(side="left", fill="x", expand=True, padx=5)
        password_toggle_button = ttk.Button(password_frame, text="Show", command=self.toggle_password_view)
        password_toggle_button.pack(side="left", padx=5)
        self.password_entry = password_entry
        self.password_toggle_button = password_toggle_button

        # Output file
        output_frame = ttk.Frame(self)
        output_frame.pack(fill="x", padx=10, pady=5)
        output_label = ttk.Label(output_frame, text="Output file:")
        output_label.pack(side="left", padx=5)
        output_entry = ttk.Entry(output_frame, state="readonly")
        output_entry.pack(side="left", fill="x", expand=True, padx=5)
        output_button = ttk.Button(output_frame, text="Save as...", command=self.get_output_file)
        output_button.pack(side="left", padx=5)
        self.output_entry = output_entry

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill="x", padx=10, pady=5)
        extract_button = ttk.Button(button_frame, text="Extract message", command=self.extract_message)
        extract_button.pack(side=tk.TOP, padx=5, anchor=tk.CENTER)

        # Extracted message
        message_frame = ttk.Frame(self)
        message_frame.pack(fill="x", padx=10, pady=5)
        message_label = ttk.Label(message_frame, text="Extracted message:")
        message_label.pack(side="left", padx=5)
        message_entry = tk.Text(message_frame, height=5, state="disabled")
        message_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.message_entry = message_entry

        # Note
        note_label = ttk.Label(self, text="Not seeing what you expected? Is the Output text file empty? Please recheck the password entered. This usually happens when the password entered is wrong.")
        note_label.configure(foreground='#FF9999', font=('Helvetica', 8, 'italic'))
        note_label.pack(pady=20)
        note_label.pack_forget()
        self.note_label = note_label



    def get_input_file(self):
        filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
        self.input_file = filedialog.askopenfilename(title="Select an input file", filetypes=filetypes)
        if self.input_file:
            self.input_entry.config(state="normal")
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.input_file)
            self.input_entry.config(state="readonly")

    def get_output_file(self):
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        self.output_file = filedialog.asksaveasfilename(title="Save output file", defaultextension=".txt", filetypes=filetypes)
        if self.output_file:
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, self.output_file)
            self.output_entry.config(state="readonly")

    def toggle_password_view(self):
        if self.password_entry["show"] == "*":
            self.password_entry.config(show="")
            self.password_toggle_button.config(text="Hide")
        else:
            self.password_entry.config(show="*")
            self.password_toggle_button.config(text="Show")

    def extract_message(self):
        if self.input_file and self.output_file:
            message = extract_message(self.input_file, self.password_entry.get(), self.output_file)
            if message:
                with open(self.output_file, "r") as f:
                    output = f.read()
                if output == "":
                    self.note_label.pack()
                else:
                    self.note_label.pack_forget()
                messagebox.showinfo("Success", f"Message successfully extracted to {self.output_file}")
                self.message_entry.config(state="normal")
                self.message_entry.delete("1.0", tk.END)
                self.message_entry.insert(tk.END, message)
                self.message_entry.config(state="disabled")
                self.input_entry.config(state="normal")
                self.input_entry.delete(0, tk.END)
                self.input_entry.config(state="readonly")
                self.output_entry.config(state="normal")
                self.output_entry.delete(0, tk.END)
                self.output_entry.config(state="readonly")
                self.password_entry.delete("0", tk.END)
                self.input_file = None
                self.output_file = None
            else:
                messagebox.showerror("Error", "No message found in input file")
        else:
            messagebox.showerror("Error", "Please select an input file and an output file")