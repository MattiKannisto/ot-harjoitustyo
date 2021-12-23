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
    def __init__(self, root):
        """[summary]

        Args:
            root ([type]): [description]
        """
        self.root = root
        self._add_menus()

        self.account_service = AccountService()

        self.main_view = MainView(
            self.root, self.account_service, self.options)
        self.login_view = LoginView(self.root, self.account_service)
        self.settings_view = SettingsView(self.root, self.account_service)
        self.create_account_view = CreateAccountView(
            self.root, self.account_service, self.options)

        self.instructions_frame = Frame(self.root)
        self.instructions_frame.grid(row=0, column=0, sticky=W+E)
        self.instructions_label = Label(
            self.instructions_frame, text="", fg="black")
        self.instructions_label.grid(row=0, column=0, sticky=W)
        self.login_timer_start = 0
        self.instructions = None
        self.active_view = None
        self.notification_update_speed = ULTRA_FAST_UPDATE_SPEED

        self.root.after(0, self._manage_views)
        self.root.after(0, self._wait_for_timer_and_return_instructions_text)

    def _manage_views(self):
        if not self.account_service.logged_in_user:
            if self.account_service.creating_new_account:
                self.main_view.inactive()
                self.login_view.inactive()
                self.settings_view.inactive()
                self.create_account_view.active()
            else:
                self.main_view.inactive()
                self.login_view.active()
                self.create_account_view.inactive()
                self.settings_view.inactive()
        else:
            if self.account_service.changing_settings:
                self.main_view.inactive()
                self.login_view.inactive()
                self.create_account_view.inactive()
                self.settings_view.active()
            else:
                self.login_view.inactive()
                self.create_account_view.inactive()
                self.settings_view.inactive()
                self.main_view.active()
        self.root.after(1, self._manage_views)

    def _get_active_view(self):
        if self.main_view.input_frame:
            return self.main_view
        elif self.login_view.frame:
            return self.login_view
        if self.create_account_view.frame:
            return self.create_account_view
        else:
            return self.settings_view

    def _get_instructions_set_default(self, view):
        if not self.instructions or len(self.instructions) == 0:
            self.instructions = view.instructions
            view.instructions = [self.instructions[0]]
            if len(self.instructions) > 1:
                self.notification_update_speed = SLOW_UPDATE_SPEED
            else:
                self.notification_update_speed = ULTRA_FAST_UPDATE_SPEED

    def _add_menus(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.options = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options)
        self.options.add_command(label="Help", command=self._help)
        self.options.add_command(label="Exit", command=self.root.destroy)

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
        if active_view == self.main_view:
            self.main_view.help()
        help_notifications = self._generate_notifications_from_string(
            help_string, "red", [])
        self.notification_update_speed = FAST_UPDATE_SPEED
        self.instructions.extend(reversed(help_notifications))

    def _wait_for_timer_and_return_instructions_text(self):
        active_view = self._get_active_view()
        self._get_instructions_set_default(active_view)
        if self.instructions and ((time.time() - self.login_timer_start) > self.notification_update_speed):
            if self.instructions_frame and len(self.instructions) > 0:
                self.instructions = self.instructions[:-1]
                self.login_timer_start = time.time()
        if self.instructions and self.instructions_frame and self.instructions_label:
            self.instructions_label.config(
                text=self.instructions[-1][0], fg=self.instructions[-1][1])
            if self.instructions[-1][0][0].isspace() and self.instructions[-1][0][1].isspace():
                self.instructions_label.grid(sticky=E)
            else:
                self.instructions_label.grid(
                    row=0, column=0, sticky=W)
        self.root.after(1, self._wait_for_timer_and_return_instructions_text)
