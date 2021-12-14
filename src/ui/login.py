from tkinter import filedialog
from tkinter import *
from entities.account import Account


class Login():
    def __init__(self, root):
        self.root = root
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=0, column=0)
        self.hello_label = Label(text="HELLO LOGIN VIEW!")
        self.hello_label.grid(row=0, column=0)

        self.exit_button = Button(
            text="Exit here", command=self.successful_exit)
        self.exit_button.grid(row=1, column=0)

    def successful_exit(self):
        self.input_frame.destroy()
