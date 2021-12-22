from tkinter import *
from services.protein_service import ProteinService
from services.dna_fragment_service import DnaFragmentService
from services.primer_service import PrimerService

class MainView():
    def __init__(self, root, account_service, options):
        self.root = root
        self.options = options
        self.account_service = account_service
        self.protein_service = ProteinService()
        self.dna_fragment_service = DnaFragmentService()
        self.input_frame = None
        self.output_frame = None
        self.name_input = None
        self.dna_fragment_name = None
        self.dna_fragment_dropdown_menu = None
        self.help_activated = False
        self.instructions = [["Welcome to designing primers!", "black"]]
        self.help_string = "Help mode activated!"

        self.root.after(0, self.check_if_buttons_should_be_active_or_inactive)

    def add_frames(self):
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=1, columnspan=5, sticky=W+E)

        self.output_frame = Frame(self.root, bg='black', pady=10)
        self.output_frame.grid(row=2, columnspan=10, sticky=W+E)
        
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

    def add_users_dna_fragments_dropdown_list(self):
        self.dna_fragment_name = StringVar(self.input_frame)
        self.dna_fragment_name.set(None)
        self.dna_fragment_being_processed_label = Label(
            self.input_frame, text="Now processing DNA fragment ")
        self.dna_fragment_being_processed_label.grid(row=1, column=0)
        users_dna_fragments_names = []
        for dna_fragment in self.dna_fragment_service.get_all_dna_fragments_by_owner(self.account_service.logged_in_user.username):
            users_dna_fragments_names.append(dna_fragment[0])
        if not users_dna_fragments_names:
            users_dna_fragments_names.append("None")
        self.dna_fragment_dropdown_menu = OptionMenu(
            self.input_frame, self.dna_fragment_name, *users_dna_fragments_names)
        self.dna_fragment_dropdown_menu.grid(
            row=1, column=1, columnspan=5, sticky=W)

    def add_notification(self, notification, labels):
        if not labels[:-1]:
            labels[0].config(text=notification[0], fg=notification[1])
        else:
            labels[-1].config(text=labels[-2].cget("text"), fg=labels[-2].cget("fg"))
            self.add_notification(notification, labels[:-1])

    def check_if_buttons_should_be_active_or_inactive(self):
        if self.input_frame:
            self.activate_add_button_if_text_fields_are_not_empty()
            self.activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected()
            if self.help_activated:
                self.help_string = "Help mode disabled!"
        self.root.after(1, self.check_if_buttons_should_be_active_or_inactive)

    def activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected(self):
        if self.dna_fragment_name:
            if self.dna_fragment_name.get() == "None" and self.help_activated == False:
                self.translate_button["state"] = DISABLED
                self.generate_primers_button["state"] = DISABLED
            else:
                self.translate_button["state"] = NORMAL
                self.generate_primers_button["state"] = NORMAL

    def activate_add_button_if_text_fields_are_not_empty(self):
        if self.name_input:
            if (not Entry.get(self.name_input) or not Entry.get(self.sequence_input)) and self.help_activated == False:
                self.add_button["state"] = DISABLED
            else:
                self.add_button["state"] = NORMAL

    def add_new_dna_fragment(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["If there are any problems in adding the DNA fragment, you will be notified of it here.", "white"], self.notification_labels)
            self.add_notification(["The added DNA fragments will be stored in a database on your PC hard disk so you can use them also later.", "white"], self.notification_labels)
            self.add_notification(["You cannot add two DNA fragments with the same name. Sequence can contain only natural nucleotides A, T, G and C.", "white"], self.notification_labels)
            self.add_notification(["You can add new DNA fragments here. The button will be activated when you have entered name and sequence.", "white"], self.notification_labels)
        else:
            notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
                Entry.get(self.name_input), Entry.get(self.sequence_input), self.account_service.logged_in_user.username)
            self.add_notification(notification, self.notification_labels)
            self.add_users_dna_fragments_dropdown_list()

    def translate(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["If there are any problems in generating the protein sequence, you will get notified of it here.", "white"], self.notification_labels)
            self.add_notification(["The protein sequence will be saved to your working directory in 'Proteins' folder.", "white"], self.notification_labels)
            self.add_notification(["You might find this functionality useful if you want to see how mutations affect the protein sequence.", "white"], self.notification_labels)
            self.add_notification(["Translate button is used to generate the protein sequence the DNA fragment codes for.", "white"], self.notification_labels)
        else:
            notification = self.protein_service.attempt_translation_and_return_notification(
                self.dna_fragment_service.get_dna_fragment_by_name_and_owner(self.dna_fragment_name.get(), self.account_service.logged_in_user.username), self.account_service.logged_in_user.directory)
            self.add_notification(notification, self.notification_labels)

    def generate_sequencing_primers(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["If there are any problems in generating the primers, you will get notified of it here.", "white"], self.notification_labels)
            self.add_notification(["The primers will be saved in your working directory in the 'primers' folder in an Excel file.", "white"], self.notification_labels)
            self.add_notification(["The primers will be by the name of the DNA fragment, the strand (forward or reverse) and number of the primer.", "white"], self.notification_labels)
            self.add_notification(["You will be able to change these values by clicking 'Settings' from the menu.", "white"], self.notification_labels)
            self.add_notification(["This is done by searching sequences in the strands that have certain length and GC content.", "white"], self.notification_labels)
            self.add_notification(["Generate sequencing primers button is used to generate sequencing primers for both strands of the DNA fragment.", "white"], self.notification_labels)
        else:
            self.primer_service = PrimerService(
                self.account_service.logged_in_user.directory, self.account_service.logged_in_user.sequencing_primer_length, self.account_service.logged_in_user.sequencing_primer_gc_content)
            notification = self.primer_service.attempt_primer_generation_and_return_notification(
                self.dna_fragment_service.get_dna_fragment_by_name_and_owner(self.dna_fragment_name.get(), self.account_service.logged_in_user.username))
            self.add_notification(notification, self.notification_labels)

    def select_dna_fragment_help(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["You can select DNA fragments that you have added previosly for analysis here.", "white"], self.notification_labels)

    def help(self):
        if self.help_activated == False:
            self.help_activated = True
            self.help_string = "Help mode disabled!"
            self.dna_fragment_dropdown_menu.destroy()
            self.dna_fragment_dropdown_fake_button = Button(
                self.input_frame, text="None   ", command=self.select_dna_fragment_help)
            self.dna_fragment_dropdown_fake_button.grid(
                row=1, column=1, columnspan=5, sticky=W)
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["To exit help mode, please click 'Help' from the menu again.", "white"], self.notification_labels)
            self.add_notification(["Welcome to help mode! Please click a button to see instructions how to see what it is used for.", "white"], self.notification_labels)
        else:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["Excellent, now let's get those sequencing primers designed!", "white"], self.notification_labels)
            self.help_string = "Help mode activated!"
            self.dna_fragment_dropdown_fake_button.destroy()
            self.add_users_dna_fragments_dropdown_list()
            self.help_activated = False

    def settings(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["Opens settings where you can change working directory, sequencing primer length and GC content, or delete your account.", "white"], self.notification_labels)
        else:
            self.account_service.changing_settings = True

    def exit(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["Click here to exit the application.", "white"], self.notification_labels)
        else:
            self.root.destroy()

    def logout(self):
        if self.help_activated == True:
            self.add_notification(["", "white"], self.notification_labels)
            self.add_notification(["Click here to logout from the application.", "white"], self.notification_labels)
        else:
            self.account_service.logout()

    def active(self):
        if not self.input_frame:
            self.add_frames()
            self.add_analysis_buttons()
            self.add_input_area()
            self.add_users_dna_fragments_dropdown_list()
            self.add_notification_area()
            self.options.delete("Exit")
            self.options.add_command(
                label="Settings", command=self.settings)
            self.options.add_command(label="Logout", command=self.logout)
            self.options.add_command(label="Exit", command=self.exit)

    def inactive(self):
        if self.input_frame:
            self.input_frame.destroy()
            self.output_frame.destroy()
            self.input_frame = None
            self.output_frame = None
            self.options.delete("Settings")
            self.options.delete("Logout")
            self.options.delete("Exit")
            self.options.add_command(label="Exit", command=self.root.destroy)
