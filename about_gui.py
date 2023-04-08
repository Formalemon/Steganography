import tkinter as tk
import webbrowser

class AboutGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # GitHub logo label
        github_logo = tk.PhotoImage(file="assets/github-mark-white.png")
        github_label = tk.Label(self, image=github_logo, cursor="hand2")
        github_label.image = github_logo
        github_label.pack(side="top", padx=10, pady=5)
        github_label.bind("<Button-1>", lambda event: webbrowser.open_new("https://github.com/Formalemon/Steganography"))

