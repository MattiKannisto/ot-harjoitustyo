from tkinter import *


class SettingsView:
    def __init__(self, root):
        self.root = root

        self.frame = Frame(self.root)

        label = Label(self.frame, text="Hello settings!")
