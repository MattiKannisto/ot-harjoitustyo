from tkinter import filedialog
from tkinter import *


class CreateAccountView():
    def __init__(self, root, account_service, options):
        self.root = root
        self.options = options
        self.account_service = account_service
        self.frame = None
        self.selected_directory = ""
        self.instructions_label = None
        self.instructions = [["Please fill in all fields:", "black"]]
        self.help_string = "Username must be unique and more than 5 characters long. Password has to be more than 10 and less than 30 characters long. Re-typed password and password have to match. Working directory needs to be selected. Please do not close the window when selecting the directory from 'X'. Click 'Create' when all fields are filled or 'Cancel' if you do not want to create new account."

    def active(self):
        if not self.frame:
            self.frame = Frame(self.root)
            self.frame.grid(row=1, column=0)

            self.username_instructions = Label(
                self.frame, text="Userame:")
            self.username_instructions.grid(row=1, column=0)
            self.username_input = Entry(self.frame)
            self.username_input.grid(row=1, column=1)

            self.password_instructions = Label(
                self.frame, text="Password:")
            self.password_instructions.grid(row=2, column=0)
            self.password_input = Entry(self.frame, show="*")
            self.password_input.grid(row=2, column=1)

            self.re_typed_password_instructions = Label(
                self.frame, text="Password re-typed:")
            self.re_typed_password_instructions.grid(row=3, column=0)
            self.re_typed_password_input = Entry(
                self.frame, show="*")
            self.re_typed_password_input.grid(row=3, column=1)

            self.working_directory_instructions = Label(
                self.frame, text="Working directory: " + self.selected_directory)
            self.working_directory_instructions.grid(row=4, column=0)
            self.working_directory_button = Button(
                self.frame, text="Browse", command=self.select_directory)
            self.working_directory_button.grid(row=4, column=1)

            self.change_to_login_frame_button = Button(
                self.frame, text="Cancel", command=self._cancel)
            self.change_to_login_frame_button.grid(row=5, column=0, sticky=E)

            self.create_user_account_button = Button(
                self.frame, text="Create", command=self.create_user_account)
            self.create_user_account_button.grid(row=5, column=1, sticky=E)

    def _cancel(self):
        self.account_service.creating_new_account = False

    def create_user_account(self):
        username = Entry.get(self.username_input)
        password = Entry.get(self.password_input)
        re_typed_password = Entry.get(self.re_typed_password_input)
        self.instructions.extend(self.account_service.create_account(username, password, re_typed_password, self.selected_directory, []))

    def select_directory(self):
        self.selected_directory = filedialog.askdirectory(initialdir="~")
 
    def inactive(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None
