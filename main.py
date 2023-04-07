import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from hide_message import hide_message
from extract_message import extract_message

class SteganographyGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Steganography GUI")
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

        # Message frame, text box, and file button
        self.message_frame = ttk.Frame(self)
        self.message_frame.pack(fill="x", padx=10, pady=5)
        self.message_label = ttk.Label(self.message_frame, text="Message:")
        self.message_label.pack(side="left", padx=5)
        self.message_entry = tk.Text(self.message_frame, height=5)
        self.message_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.message_file_button = ttk.Button(self.message_frame, text="Add from file...", command=self.get_message_file)
        self.message_file_button.pack(side="left", padx=5)

        # Output file
        output_frame = ttk.Frame(self)
        output_frame.pack(fill="x", padx=10, pady=5)
        output_label = ttk.Label(output_frame, text="Output file:")
        output_label.pack(side="left", padx=5)
        output_entry = ttk.Entry(output_frame, state="readonly")
        output_entry.pack(side="left", fill="x", expand=True, padx=5)
        output_button = ttk.Button(output_frame, text="Browse...", command=self.get_output_file)
        output_button.pack(side="left", padx=5)
        self.output_entry = output_entry

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill="x", padx=10, pady=5)
        hide_button = ttk.Button(button_frame, text="Hide message", command=self.hide_message)
        hide_button.pack(side="left", padx=5)
        extract_button = ttk.Button(button_frame, text="Extract message", command=self.extract_message)
        extract_button.pack(side="left", padx=5)

    def get_input_file(self):
        filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
        self.input_file = filedialog.askopenfilename(title="Select an input file", filetypes=filetypes)
        if self.input_file:
            self.input_entry.config(state="normal")
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.input_file)
            self.input_entry.config(state="readonly")


    def get_message_file(self):
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        self.message_file = filedialog.askopenfilename(title="Select a message file", filetypes=filetypes)
        if self.message_file:
            with open(self.message_file, "r") as f:
                message = f.read()
                self.message_entry.insert(tk.END, message)

    def get_output_file(self):
        filetypes = (("PNG files", "*.png"), ("All files", "*.*"))
        self.output_file = filedialog.asksaveasfilename(title="Save output file", defaultextension=".png", filetypes=filetypes)
        if self.output_file:
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, self.output_file)
            self.output_entry.config(state="readonly")

    def hide_message(self):
        message = self.message_box.get("1.0", tk.END)
        if message and self.input_file and self.output_file:
            hide_message(self.input_file, message, None, self.output_file)
            messagebox.showinfo("Success", f"Message successfully hidden in {self.output_file}")
        else:
            messagebox.showerror("Error", "Please select an input file, an output file, and enter a message")

    def extract_message(self):
        if self.input_file and self.output_file:
            message = extract_message(self.input_file, self.output_file)
            if message:
                with open(self.output_file, "w") as f:
                    f.write(message)
                messagebox.showinfo("Success", f"Message successfully extracted to {self.output_file}")
            else:
                messagebox.showerror("Error", "No message found in input file")
        else:
            messagebox.showerror("Error", "Please select an input file and an output file")

root = tk.Tk()
app = SteganographyGUI(master=root)
app.mainloop()