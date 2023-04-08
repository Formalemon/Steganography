import tkinter as tk
import webbrowser

class AboutGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # GitHub logo label
        self.github_logo = tk.PhotoImage(file="assets/github-mark-white.png")
        self.github_logo_light = tk.PhotoImage(file="assets/github-mark.png")
        self.github_label = tk.Label(self, image=self.github_logo, cursor="hand2")
        self.github_label.image = self.github_logo
        self.github_label.pack(side="top", padx=10, pady=5)
        self.github_label.bind("<Button-1>", lambda event: webbrowser.open_new("https://github.com/Formalemon/Steganography"))
        
    def update_logo(self, theme):
        if theme == "darkly":
            self.github_label.config(image=self.github_logo)
        else:
            self.github_label.config(image=self.github_logo_light)

