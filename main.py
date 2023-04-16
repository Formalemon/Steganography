import tkinter as tk
import ttkbootstrap as ttk
import webbrowser
import hide_gui
import extract_gui
import about_gui
import password_gui


class SteganographyGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Steganography Tool")
        self.master.geometry("713x400")
        self.master.resizable(False, False)
        self.pack(fill=tk.BOTH, expand=True)
        self.style = ttk.Style()
        self.style.theme_use("darkly")
        self.create_widgets()

    def create_widgets(self):
        # Create a top-level frame to hold the buttons and the frames
        top_frame = ttk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the Home button
        home_button = ttk.Button(top_frame, text="Home", command=self.show_home_frame)
        home_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Hide button
        hide_button = ttk.Button(top_frame, text="Hide Text", command=self.show_hide_frame)
        hide_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Extract button
        extract_button = ttk.Button(top_frame, text="Extract Text", command=self.show_extract_frame)
        extract_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the About button
        about_button = ttk.Button(top_frame, text="About", command=self.show_about_frame)
        about_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the Password Generation button
        password_button = ttk.Button(top_frame, text="Password Generation", command=self.show_password_frame)
        password_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a drop-down menu for themes
        theme_frame = ttk.Frame(top_frame)
        theme_frame.pack(side=tk.RIGHT, padx=10, pady=5)
        theme_label = ttk.Label(theme_frame, text="Theme:")
        theme_label.pack(side="left", pady=5)
        theme_var = tk.StringVar()
        theme_dropdown = ttk.Combobox(
            theme_frame, 
            textvariable=theme_var, 
            values=["darkly", "flatly", "litera"], 
            state="readonly", 
            width=8,
        )
        theme_dropdown.pack(side=tk.LEFT, padx=5, pady=5)
        theme_dropdown.current(0)
        theme_dropdown.bind("<<ComboboxSelected>>", lambda event, theme_var=theme_var: self.change_theme(theme_var.get()))

        # Create the home frame
        self.home_frame = ttk.Frame(self)
        self.home_frame.pack(fill=tk.BOTH, expand=True)

        steganography_text = "Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video."
        home_label = ttk.Label(self.home_frame, text=f"Welcome to Steganography APP!\n\n{steganography_text}")
        home_label.pack(padx=10, pady=10)

        tutorial_label = ttk.Label(self.home_frame, text="Click here for a short tutorial on Steganography", foreground="blue", cursor="hand2")
        tutorial_label.pack(padx=10, pady=10)
        tutorial_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://en.wikipedia.org/wiki/Steganography"))

        # Create the hide frame
        self.hide_frame = hide_gui.HideGUI(self)
        self.hide_frame.pack_forget()

        # Create the extract frame
        self.extract_frame = extract_gui.ExtractGUI(self)
        self.extract_frame.pack_forget()

        # Create the about frame
        self.about_frame = about_gui.AboutGUI(self)
        self.about_frame.pack_forget()

        # Create the password generation frame
        self.password_frame = password_gui.PasswordGUI(self)
        self.password_frame.pack_forget()

    def show_home_frame(self):
        self.hide_frame.pack_forget()
        self.extract_frame.pack_forget()
        self.about_frame.pack_forget()
        self.password_frame.pack_forget()
        self.home_frame.pack(fill=tk.BOTH, expand=True)

    def show_hide_frame(self):
        self.home_frame.pack_forget()
        self.extract_frame.pack_forget()
        self.about_frame.pack_forget()
        self.password_frame.pack_forget()
        self.hide_frame.pack(fill=tk.BOTH, expand=True)

    def show_extract_frame(self):
        self.home_frame.pack_forget()
        self.hide_frame.pack_forget()
        self.about_frame.pack_forget()
        self.password_frame.pack_forget()
        self.extract_frame.pack(fill=tk.BOTH, expand=True)

    def show_about_frame(self):
        self.home_frame.pack_forget()
        self.hide_frame.pack_forget()
        self.extract_frame.pack_forget()
        self.password_frame.pack_forget()
        self.about_frame.pack(fill=tk.BOTH, expand=True)

    def show_password_frame(self):
        self.home_frame.pack_forget()
        self.hide_frame.pack_forget()
        self.extract_frame.pack_forget()
        self.about_frame.pack_forget()
        self.password_frame.pack(fill=tk.BOTH, expand=True)

    def change_theme(self, theme):
        self.master.style = ttk.Style(theme=theme)
        self.master.style.theme_use(theme)
        self.about_frame.update_logo(theme)

root = tk.Tk()
app = SteganographyGUI(master=root)
app.mainloop()
