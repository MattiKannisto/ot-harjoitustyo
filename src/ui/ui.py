import time
from tkinter import *
from services.account_service import AccountService
from ui.main_view import MainView
from ui.settings_view import SettingsView
from ui.login_view import LoginView
from ui.create_account_view import CreateAccountView

SLOW_UPDATE_SPEED = 2
FAST_UPDATE_SPEED = 0.1
ULTRA_FAST_UPDATE_SPEED = 0.01


class UserInterface():
    """A class responsible for creating common elements of all views of the application and for switching between different views
    """

    def __init__(self, root):
        """Constructor for the class

        Args:
            root: root window of the application
        """
        self._root = root
        self._add_menus()

        self._account_service = AccountService()

        self._main_view = MainView(self._root, self._account_service, self.options)
        self._login_view = LoginView(self._root, self._account_service)
        self._settings_view = SettingsView(self._root, self._account_service)
        self._create_account_view = CreateAccountView(self._root, self._account_service)

        self._instructions_frame = Frame(self._root)
        self._instructions_frame.grid(row=0, column=0, sticky=W+E)
        self._instructions_label = Label(self._instructions_frame, text="", fg="black")
        self._instructions_label.grid(row=0, column=0, sticky=W)
        self._timer_start = 0
        self._instructions = None
        self._active_view = None
        self._notification_update_speed = ULTRA_FAST_UPDATE_SPEED

        self._root.after(0, self._manage_views)
        self._root.after(0, self._wait_for_timer_and_return_instructions_text)

    def _manage_views(self):
        if not self._account_service.logged_in_user:
            if self._account_service.creating_new_account:
                self._main_view.inactive()
                self._login_view.inactive()
                self._settings_view.inactive()
                self._create_account_view.active()
            else:
                self._main_view.inactive()
                self._login_view.active()
                self._create_account_view.inactive()
                self._settings_view.inactive()
        else:
            if self._account_service.changing_settings:
                self._main_view.inactive()
                self._login_view.inactive()
                self._create_account_view.inactive()
                self._settings_view.active()
            else:
                self._login_view.inactive()
                self._create_account_view.inactive()
                self._settings_view.inactive()
                self._main_view.active()
        self._root.after(1, self._manage_views)

    def _get_active_view(self):
        if self._main_view.input_frame:
            return self._main_view
        elif self._login_view.frame:
            return self._login_view
        if self._create_account_view.frame:
            return self._create_account_view
        else:
            return self._settings_view

    def _get_instructions_set_default(self, view):
        if not self._instructions or len(self._instructions) == 0:
            self._instructions = view.instructions
            view.instructions = [self._instructions[0]]
            if len(self._instructions) > 1:
                self._notification_update_speed = SLOW_UPDATE_SPEED
            else:
                self._notification_update_speed = ULTRA_FAST_UPDATE_SPEED

    def _add_menus(self):
        self.menu = Menu(self._root)
        self._root.config(menu=self.menu)
        self.options = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options)
        self.options.add_command(label="Help", command=self._help)
        self.options.add_command(label="Exit", command=self._root.destroy)

    def _generate_notifications_from_string(self, string, color, list):
        for i in range(len(string)+40):
            help_string = ""
            if i < 40:
                for j in range(40-i):
                    help_string += " "
                help_string = help_string + string[:i]
            elif (len(string)-i) < 40:
                help_string = help_string + string[i-40:i]
                for j in range(40-i):
                    help_string += " "
            else:
                help_string = help_string + string[i-40:i]
            list.append([help_string, color])
        return list

    def _help(self):
        active_view = self._get_active_view()
        help_string = active_view.help_string
        if active_view == self._main_view:
            self._main_view.help()
        help_notifications = self._generate_notifications_from_string(
            help_string, "red", [])
        self._notification_update_speed = FAST_UPDATE_SPEED
        self._instructions.extend(reversed(help_notifications))

    def _wait_for_timer_and_return_instructions_text(self):
        active_view = self._get_active_view()
        self._get_instructions_set_default(active_view)
        if self._instructions and ((time.time() - self._timer_start) > self._notification_update_speed):
            if self._instructions_frame and len(self._instructions) > 0:
                self._instructions = self._instructions[:-1]
                self._timer_start = time.time()
        if self._instructions and self._instructions_frame and self._instructions_label:
            self._instructions_label.config(
                text=self._instructions[-1][0], fg=self._instructions[-1][1])
            if self._instructions[-1][0][0].isspace() and self._instructions[-1][0][1].isspace():
                self._instructions_label.grid(sticky=E)
            else:
                self._instructions_label.grid(
                    row=0, column=0, sticky=W)
        self._root.after(1, self._wait_for_timer_and_return_instructions_text)
