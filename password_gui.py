import tkinter as tk
from password_gui_right_half import PassGenRightHalf
from password_gui_left_half import PassGenLeftHalf

class PasswordGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.right_half = PassGenRightHalf(self)
        self.left_half = PassGenLeftHalf(self, right_half=self.right_half)

        self.left_half.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_half.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
