from tkinter import filedialog
from tkinter import *


class CreateAccountView():
    """A class responsible for creating the view for creating a new user account
    """

    def __init__(self, root, account_service):
        """Constructor for the class

        Args:
            root: Root window of the application
            account_service: Account service object common to all views. Information which view should be displayed is stored in its internal state
        """

        self._root = root
        self._account_service = account_service
        self.frame = None
        self._selected_directory = ""
        self._instructions_label = None
        self.instructions = [["Please fill in all fields:", "black"]]
        self.help_string = "Name must be unique and more than 5 characters long. Password has to be more than 10 and less than 30 characters long. Re-typed password and password have to match. Working directory needs to be selected. Please do not close the window when selecting the directory from 'X'. Click 'Create' when all fields are filled or 'Cancel' if you do not want to create new account."

    def _cancel(self):
        self._account_service.creating_new_account = False

    def _create_user_account(self):
        name = Entry.get(self.name_input)
        password = Entry.get(self.password_input)
        re_typed_password = Entry.get(self.re_typed_password_input)
        self.instructions.extend(self._account_service.create_account(
            name, password, re_typed_password, self._selected_directory, []))

    def _select_directory(self):
        self._selected_directory = filedialog.askdirectory(initialdir="~")

    def active(self):
        """A method for activating the view by creating a frame and adding all components to it
        """

        if not self.frame:
            self.frame = Frame(self._root)
            self.frame.grid(row=1, column=0)

            self.name_instructions = Label(self.frame, text="Userame:")
            self.name_instructions.grid(row=1, column=0)
            self.name_input = Entry(self.frame)
            self.name_input.grid(row=1, column=1)

            self.password_instructions = Label(self.frame, text="Password:")
            self.password_instructions.grid(row=2, column=0)
            self.password_input = Entry(self.frame, show="*")
            self.password_input.grid(row=2, column=1)

            self.re_typed_password_instructions = Label(self.frame, text="Password re-typed:")
            self.re_typed_password_instructions.grid(row=3, column=0)
            self.re_typed_password_input = Entry(self.frame, show="*")
            self.re_typed_password_input.grid(row=3, column=1)

            self.working_directory_instructions = Label(self.frame, text="Working directory: ")
            self.working_directory_instructions.grid(row=4, column=0)
            self.working_directory_button = Button(self.frame, text="Browse", command=self._select_directory)
            self.working_directory_button.grid(row=4, column=1)

            self.change_to_login_frame_button = Button(
                self.frame, text="Cancel", command=self._cancel)
            self.change_to_login_frame_button.grid(row=5, column=0, sticky=E)

            self._create_user_account_button = Button(
                self.frame, text="Create", command=self._create_user_account)
            self._create_user_account_button.grid(row=5, column=1, sticky=E)

    def inactive(self):
        """A method for inactivating the view by deleting its frame
        """

        if self.frame:
            self.frame.destroy()
            self.frame = None
