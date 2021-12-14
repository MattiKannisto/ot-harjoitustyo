import time
from tkinter import filedialog
from tkinter import *
from services.account_service import AccountService
from services.protein_service import ProteinService
from services.dna_fragment_service import DnaFragmentService
from services.primer_service import PrimerService
from ui.settings import SettingsView
from ui.login import Login


ALLOWED_SEQUENCING_PRIMER_LENGTH_RANGE = list(range(15, 26))
ALLOWED_SEQUENCING_PRIMER_GC_CONTENT_RANGE = list(range(40, 61))


class UserInterface():
    def __init__(self, root):
        self.root = root
        self.account_service = AccountService()
        self.protein_service = ProteinService()
        self.dna_fragment_service = DnaFragmentService()
        self.notifications = []
        self.active_view = None
        self.logged_in_user = None
        self.login_frame = None
        self.name_input = None
        self.dna_fragment_name = None
        self.dna_fragment_dropdown_menu = None
        self.login_timer_start = 0

#        self.general_instructions = Label(
#            self.input_frame, text="Add new DNA fragment:")
#        self.general_instructions.grid(row=0, column=0, columnspan=2, sticky=W)

        self.add_menus()
        self.add_frames()
        self.login()
#         self.active_view = Login(self.root)
        self.root.after(0, self.check_if_buttons_should_be_active_or_inactive)

    def updated_elements(self):
        if self.logged_in_user:
            self.check_if_buttons_should_be_active_or_inactive()
#        elif self.login_frame:
#            self.wait_for_timer_and_return_login_instructions_text()

    def add_frames(self):
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=0, columnspan=5, sticky=W+E)

        self.output_frame = Frame(self.root, bg='black', pady=10)
        self.output_frame.grid(row=2, columnspan=10, sticky=W+E)

    def login(self):
        self.login_frame = Frame(self.root)
        self.login_frame.grid(row=0, column=0)

        self.login_instructions = Label(
            self.login_frame, text="Please log in by typing your credentials below:", fg="black")
        self.login_instructions.grid(row=0, column=0, columnspan=10, sticky=W)

        self.username_instructions = Label(self.login_frame, text="Userame:")
        self.username_instructions.grid(row=1, column=0)
        self.username_input = Entry(self.login_frame)
        self.username_input.grid(row=1, column=1)

        self.password_instructions = Label(self.login_frame, text="Password:")
        self.password_instructions.grid(row=1, column=2)
        self.password_input = Entry(self.login_frame, show="*")
        self.password_input.grid(row=1, column=3)

        self.login_button = Button(
            self.login_frame, text="Login", command=self.exit_from_login)
        self.login_button.grid(row=1, column=4)

        self.create_account_button = Button(
            self.login_frame, text="Create user account", command=self.change_to_create_user_account_frame)
        self.create_account_button.grid(
            row=2, column=3, columnspan=2, sticky=E)

    def change_to_create_user_account_frame(self):
        self.login_frame.destroy()
        self.login_instructions = None

        self.create_user_account_frame = Frame(self.root)
        self.create_user_account_frame.grid(row=0, column=0)

        self.create_user_account_instructions = Label(
            self.create_user_account_frame, text="Please fill in all fields:", fg="black")
        self.create_user_account_instructions.grid(
            row=0, column=0, columnspan=10, sticky=W)

        self.username_instructions = Label(
            self.create_user_account_frame, text="Userame:")
        self.username_instructions.grid(row=1, column=0)
        self.username_input = Entry(self.create_user_account_frame)
        self.username_input.grid(row=1, column=1)

        self.password_instructions = Label(
            self.create_user_account_frame, text="Password:")
        self.password_instructions.grid(row=2, column=0)
        self.password_input = Entry(self.create_user_account_frame, show="*")
        self.password_input.grid(row=2, column=1)

        self.re_typed_password_instructions = Label(
            self.create_user_account_frame, text="Password re-typed:")
        self.re_typed_password_instructions.grid(row=3, column=0)
        self.re_typed_password_input = Entry(
            self.create_user_account_frame, show="*")
        self.re_typed_password_input.grid(row=3, column=1)

        self.working_directory_instructions = Label(
            self.create_user_account_frame, text="Select a working directory:")
        self.working_directory_instructions.grid(row=4, column=0)
        self.working_directory_button = Button(
            self.create_user_account_frame, text="Browse", command=self.select_directory)
        self.working_directory_button.grid(row=4, column=1)

        self.change_to_login_frame_button = Button(
            self.create_user_account_frame, text="Cancel", command=self.change_to_login_frame)
        self.change_to_login_frame_button.grid(row=5, column=0, sticky=E)

        self.create_user_account_button = Button(
            self.create_user_account_frame, text="Create", command=self.create_user_account)
        self.create_user_account_button.grid(row=5, column=1, sticky=E)

    def select_directory(self):
        self.selected_directory = filedialog.askdirectory()

    def change_to_login_frame(self):
        self.create_user_account_frame.destroy()
        self.login()

    def open_settings_window(self):
        self.settings_window = Toplevel(self.root)
        change_working_directory_label = Label(
            self.settings_window, text="Change working directory:")
        change_working_directory_label.grid(row=0, column=0, sticky=W)
        change_working_directory_button = Button(
            self.settings_window, text="Browse", command=self.change_working_directory)
        change_working_directory_button.grid(row=0, column=1)

        sequencing_primer_length_instructions = Label(
            self.settings_window, text="Change sequencing primer length:")
        sequencing_primer_length_instructions.grid(row=1, column=0)
        self.primer_length = StringVar()
        self.primer_length.set(
            str(self.logged_in_user.sequencing_primer_length))
        sequencing_primer_length_dropdown_menu = OptionMenu(
            self.settings_window, self.primer_length, *ALLOWED_SEQUENCING_PRIMER_LENGTH_RANGE)
        sequencing_primer_length_dropdown_menu.grid(row=1, column=1)

        gc_content_instructions = Label(
            self.settings_window, text="Change sequencing primer GC content (%):")
        gc_content_instructions.grid(row=2, column=0)
        self.gc_content = StringVar()
        self.gc_content.set(
            str(int(self.logged_in_user.sequencing_primer_gc_content*100)))
        gc_content_dropdown_menu = OptionMenu(
            self.settings_window, self.gc_content, *ALLOWED_SEQUENCING_PRIMER_GC_CONTENT_RANGE)
        gc_content_dropdown_menu.grid(row=2, column=1)

        delete_account_button = Button(
            self.settings_window, text="Delete account", command=self.delete_account)
        delete_account_button.grid(row=3, column=0)

        done_button = Button(self.settings_window, text="Done",
                             command=self.save_settings_and_exit)
        done_button.grid(row=3, column=1)

    def save_settings_and_exit(self):
        self.logged_in_user.sequencing_primer_length = int(
            self.primer_length.get())
        self.logged_in_user.sequencing_primer_gc_content = float(
            self.gc_content.get())/100

        self.account_service.update_account(self.logged_in_user)

        self.settings_window.destroy()

    def change_working_directory(self):
        self.directory = filedialog.askdirectory(
            initialdir=self.logged_in_user.directory)
        if self.logged_in_user:
            self.logged_in_user.directory = self.directory

    def create_user_account(self):
        username = Entry.get(self.username_input)
        password = Entry.get(self.password_input)
        re_typed_password = Entry.get(self.re_typed_password_input)
        if password != re_typed_password:
            print("salasanat ei täsmää")
        elif self.account_service.username_already_in_use(username):
            print("käyttäjätunnus jo käytössä")
        else:
            self.account_service.create_account(
                username, password, self.selected_directory)
        self.change_to_login_frame()

    def exit_from_login(self):
        user_account = self.account_service.get_account_by_name(
            Entry.get(self.username_input))
        password = Entry.get(self.password_input)
        if user_account and password == user_account.password:
            self.logged_in_user = user_account
            self.login_frame.destroy()
            self.add_analysis_buttons()
            self.add_input_area()
            self.add_users_dna_fragments_dropdown_list()
            self.add_notification_area()
            self.options.add_command(
                label="Settings", command=self.open_settings_window)
            self.options.add_command(label="Logout", command=self.logout)
        else:
            self.login_timer_start = time.time()
            self.login_instructions.config(
                text="INCORRECT CREDENTIALS", fg="red")

    def wait_for_timer_and_return_login_instructions_text(self):
        if (time.time() - self.login_timer_start) > 2:
            self.login_instructions.config(
                text="Please log in by typing your credentials below:", fg="black")
            self.root.after(
                1, self.wait_for_timer_and_return_login_instructions_text)

    def delete_account(self):
        self.account_service.delete_account(self.logged_in_user)
        self.settings_window.destroy()
        self.logout()

    def add_input_area(self):
        self.name_instructions = Label(self.input_frame, text="Name:")
        self.name_instructions.grid(row=0, column=0)
        self.name_input = Entry(self.input_frame)
        self.name_input.grid(row=0, column=1)

        self.sequence_label = Label(self.input_frame, text="Sequence:")
        self.sequence_label.grid(row=0, column=2)
        self.sequence_input = Entry(self.input_frame)
        self.sequence_input.grid(row=0, column=3)

        self.add_button = Button(
            self.input_frame, text="Add new DNA fragment", command=self.add_new_dna_fragment)
        self.add_button.grid(row=0, column=4)

    def add_analysis_buttons(self):
        self.translate_button = Button(
            self.input_frame, text="Translate", command=self.translate)
        self.translate_button.grid(row=2, column=0)

        self.generate_primers_button = Button(
            self.input_frame, text="Generate sequencing primers", command=self.generate_sequencing_primers)
        self.generate_primers_button.grid(row=2, column=1)

    def add_notification_area(self):
        self.notification_labels = []
        for i in range(30):
            self.notification_labels.append(
                Label(self.output_frame, bg='black', fg='white', text=""))
            self.notification_labels[i].grid(
                row=3+i, column=0, columnspan=100, sticky=W)

    def add_menus(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.options = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options)
        self.options.add_command(label="Exit", command=self.quit)

    def logout(self):
        self.logged_in_user = None
        self.options.delete("Settings")
        self.options.delete("Logout")
        self.input_frame.destroy()
        self.output_frame.destroy()
        self.add_frames()
        self.login()

    def add_users_dna_fragments_dropdown_list(self):
        self.dna_fragment_name = StringVar(self.input_frame)
        self.dna_fragment_name.set(None)
        self.dna_fragment_being_processed_label = Label(
            self.input_frame, text="")
        self.dna_fragment_being_processed_label.grid(row=1, column=0)
        users_dna_fragments_names = []
        for dna_fragment in self.dna_fragment_service.get_all_dna_fragments():
            users_dna_fragments_names.append(dna_fragment[0])
        if len(users_dna_fragments_names) == 0:
            self.dna_fragment_being_processed_label.config(
                text="No DNA fragments added")
        else:
            self.dna_fragment_being_processed_label.config(
                text="Now processing DNA fragment ")
            self.dna_fragment_dropdown_menu = OptionMenu(
                self.input_frame, self.dna_fragment_name, *users_dna_fragments_names)
            self.dna_fragment_dropdown_menu.grid(
                row=1, column=1, columnspan=5, sticky=W)

    def add_notification(self, notification):
        self.notifications.insert(0, notification)

    def update_notification_area(self):
        for i in range(len(self.notification_labels)):
            if i < len(self.notifications):
                self.notification_labels[i].config(
                    text=self.notifications[i][0], fg=self.notifications[i][1])

    def check_if_buttons_should_be_active_or_inactive(self):
        self.activate_add_button_if_text_fields_are_not_empty()
        self.activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected()
        self.root.after(1, self.check_if_buttons_should_be_active_or_inactive)

    def activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected(self):
        if self.dna_fragment_name:
            if self.dna_fragment_name.get() == "None":
                self.translate_button["state"] = DISABLED
                self.generate_primers_button["state"] = DISABLED
            else:
                self.translate_button["state"] = NORMAL
                self.generate_primers_button["state"] = NORMAL

    def activate_add_button_if_text_fields_are_not_empty(self):
        if self.name_input:
            if not Entry.get(self.name_input) or not Entry.get(self.sequence_input):
                self.add_button["state"] = DISABLED
            else:
                self.add_button["state"] = NORMAL

    def ask_for_user_directory_if_not_specified(self):
        if self.logged_in_user.directory == "":
            self.logged_in_user.directory = filedialog.askdirectory()

    def add_new_dna_fragment(self):
        name = Entry.get(self.name_input)
        sequence = Entry.get(self.sequence_input)
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
            name, sequence)
        self.add_notification(notification)
        self.add_users_dna_fragments_dropdown_list()
        self.update_notification_area()

    def translate(self):
        self.ask_for_user_directory_if_not_specified()
        notification = self.protein_service.attempt_translation_and_return_notification(
            self.dna_fragment_service.get_dna_fragment_by_name(self.dna_fragment_name.get()), self.logged_in_user.directory)
        self.add_notification(notification)
        self.update_notification_area()

    def generate_sequencing_primers(self):
        self.ask_for_user_directory_if_not_specified()
        self.primer_service = PrimerService(
            self.logged_in_user.directory, self.logged_in_user.sequencing_primer_length, self.logged_in_user.sequencing_primer_gc_content)
        notification = self.primer_service.attempt_primer_generation_and_return_notification(
            self.dna_fragment_service.get_dna_fragment_by_name(self.dna_fragment_name.get()))
        self.add_notification(notification)
        self.update_notification_area()

    def quit(self):
        self.root.destroy()
