from tkinter import *
from tkinter import filedialog

PRIMER_LENGTH_RANGE = list(range(15, 26))
PRIMER_GC_CONTENT_RANGE = list(range(40, 61))


class SettingsView:
    """A class responsible for creating the view for changing settings
    """

    def __init__(self, root, account_service):
        """Constructor of the class

        Args:
            root: Root window of the application
            account_service: Account service object common to all views. Information which view should be displayed is stored in its internal state
        """

        self._root = root
        self._account_service = account_service
        self.frame = None
        self.instructions = [["Settings:", "black"]]
        self.help_string = "You can change your working directory here but please do not close the window from 'X'. For optimal primer length and GC content, please see DNA sequencing service providers instructions. DO NOT CLICK 'Delete account' UNLESS ABSOLUTELY SURE. Your output files will not be deleted but all other information associated with your account will be deleted from the databases."

    def _save_settings_and_exit(self):
        self._account_service.logged_in_user.primer_length = int(self.primer_length.get())
        self._account_service.logged_in_user.primer_gc_content = float(self.gc_content.get())/100

        self._account_service.update_account()
        self._account_service.changing_settings = False

    def _change_working_directory(self):
        if self._account_service.logged_in_user:
            directory = filedialog.askdirectory(initialdir=self._account_service.logged_in_user.directory)
            if directory:
                self._account_service.logged_in_user.directory = directory

    def active(self):
        """A method for activating the view by creating a frame and adding all components to it
        """

        if not self.frame:
            self.frame = Frame(self._root)
            self.frame.grid(row=1, column=0)

            change_working_directory_label = Label(self.frame, text="Working directory: ")
            change_working_directory_label.grid(row=0, column=0, sticky=W)
            change_working_directory_button = Button(self.frame, text="Browse", command=self._change_working_directory)
            change_working_directory_button.grid(row=0, column=1)

            primer_length_instructions = Label(self.frame, text="Change sequencing primer length:")
            primer_length_instructions.grid(row=1, column=0)
            self.primer_length = StringVar()
            self.primer_length.set(str(self._account_service.logged_in_user.primer_length))
            primer_length_dropdown_menu = OptionMenu(self.frame, self.primer_length, *PRIMER_LENGTH_RANGE)
            primer_length_dropdown_menu.grid(row=1, column=1)

            gc_content_instructions = Label(self.frame, text="Change sequencing primer GC content (%):")
            gc_content_instructions.grid(row=2, column=0)
            self.gc_content = StringVar()
            self.gc_content.set(str(int(self._account_service.logged_in_user.primer_gc_content*100)))
            gc_content_dropdown_menu = OptionMenu(self.frame, self.gc_content, *PRIMER_GC_CONTENT_RANGE)
            gc_content_dropdown_menu.grid(row=2, column=1)

            delete_account_button = Button(self.frame, text="Delete account", command=self._account_service.delete_account)
            delete_account_button.grid(row=3, column=0)

            done_button = Button(self.frame, text="Done", command=self._save_settings_and_exit)
            done_button.grid(row=3, column=1)

    def inactive(self):
        """A method for inactivating the view by deleting its frame
        """

        if self.frame:
            self.frame.destroy()
            self.frame = None
