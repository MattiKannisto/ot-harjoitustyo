from tkinter import *


class LoginView():
    def __init__(self, root, account_service):
        self.root = root
        self.account_service = account_service
        self.frame = None
        self.help_string = "If you do not have created an account, please click 'Create user account' button. Otherwise you should enter your name and password below to log in."
        self.instructions = [
            ["Please log in by typing your credentials below:", "black"]]

    def active(self):
        if not self.frame:
            self.frame = Frame(self.root)
            self.frame.grid(row=1, column=0)

            self.name_instructions = Label(self.frame, text="name:")
            self.name_instructions.grid(row=1, column=0)
            self.name_input = Entry(self.frame)
            self.name_input.grid(row=1, column=1)

            self.password_instructions = Label(self.frame, text="Password:")
            self.password_instructions.grid(row=1, column=2)
            self.password_input = Entry(self.frame, show="*")
            self.password_input.grid(row=1, column=3)

            self.login_button = Button(
                self.frame, text="Login", command=self._attempt_login)
            self.login_button.grid(row=1, column=4)

            self.create_account_button = Button(
                self.frame, text="Create user account", command=self._change_to_create_user_account_view)
            self.create_account_button.grid(
                row=2, column=3, columnspan=2, sticky=E)

    def _attempt_login(self):
        name = Entry.get(self.name_input)
        password = Entry.get(self.password_input)
        self.account_service.login(name, password)
        if not self.account_service.logged_in_user:
            self.instructions.append(["INCORRECT CREDENTIALS", "red"])

    def _change_to_create_user_account_view(self):
        self.account_service.creating_new_account = True

    def inactive(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None
