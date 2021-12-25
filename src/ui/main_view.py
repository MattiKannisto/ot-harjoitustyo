from tkinter import *
from services.protein_service import ProteinService
from services.dna_fragment_service import DnaFragmentService
from services.primer_service import PrimerService


class MainView():
    def __init__(self, root, account_service, options):
        """Constructor for the class

        Args:
            root: Root window of the application
            account_service: Account service object common to all views. Information which view should be displayed is stored in its internal state
            options: Options menu of the application
        """

        self._root = root
        self._options = options
        self._account_service = account_service
        self._protein_service = ProteinService()
        self._dna_fragment_service = DnaFragmentService()
        self._primer_service = PrimerService()
        self.input_frame = None
        self._output_frame = None
        self._name_input = None
        self._dna_fragment_name = None
        self._dna_fragment_dropdown_menu = None
        self._help_activated = False
        self.instructions = [["Welcome to designing primers!", "black"]]
        self.help_string = "Help mode activated!"

        self._root.after(0, self._check_if_buttons_should_be_active_or_inactive)
        self._root.after(0, self._remove_dna_fragments_and_primers_from_databases_if_account_deleted)

    def _add_frames(self):
        self.input_frame = Frame(self._root)
        self.input_frame.grid(row=1, columnspan=5, sticky=W+E)

        self._output_frame = Frame(self._root, bg='black', pady=10)
        self._output_frame.grid(row=2, columnspan=10, sticky=W+E)

    def _add_input_area(self):
        self.name_instructions = Label(self.input_frame, text="Name:")
        self.name_instructions.grid(row=0, column=0)
        self._name_input = Entry(self.input_frame)
        self._name_input.grid(row=0, column=1)

        self.sequence_label = Label(self.input_frame, text="Sequence:")
        self.sequence_label.grid(row=0, column=2)
        self.sequence_input = Entry(self.input_frame)
        self.sequence_input.grid(row=0, column=3)

        self.add_button = Button(
            self.input_frame, text="Add new DNA fragment", command=self._add_new_dna_fragment)
        self.add_button.grid(row=0, column=4)

    def _add_analysis_buttons(self):
        self.translate_button = Button(
            self.input_frame, text="Translate", command=self._translate)
        self.translate_button.grid(row=2, column=0)

        self.generate_primers_button = Button(
            self.input_frame, text="Generate sequencing primers", command=self._generate_primerss)
        self.generate_primers_button.grid(row=2, column=1)

    def _add_notification_area(self):
        self.notification_labels = []
        for i in range(30):
            self.notification_labels.append(Label(self._output_frame, bg='black', fg='white', text=""))
            self.notification_labels[i].grid(row=3+i, column=0, columnspan=100, sticky=W)

    def _add_users_dna_fragments_dropdown_list(self):
        self._dna_fragment_name = StringVar(self.input_frame)
        self._dna_fragment_name.set(None)
        self._dna_fragment_being_processed_label = Label(
            self.input_frame, text="Now processing DNA fragment ")
        self._dna_fragment_being_processed_label.grid(row=1, column=0)
        users_dna_fragments_names = []
        for dna_fragment in self._dna_fragment_service.get_all_dna_fragments_by_owner_name(self._account_service.logged_in_user.name):
            users_dna_fragments_names.append(dna_fragment[0])
        if not users_dna_fragments_names:
            users_dna_fragments_names.append("None")
        self._dna_fragment_dropdown_menu = OptionMenu(
            self.input_frame, self._dna_fragment_name, *users_dna_fragments_names)
        self._dna_fragment_dropdown_menu.grid(
            row=1, column=1, columnspan=5, sticky=W)

    def _add_notification(self, notification, labels):
        if not labels[:-1]:
            labels[0].config(text=notification[0], fg=notification[1])
        else:
            labels[-1].config(text=labels[-2].cget("text"), fg=labels[-2].cget("fg"))
            self._add_notification(notification, labels[:-1])

    def _check_if_buttons_should_be_active_or_inactive(self):
        if self.input_frame:
            self._activate_add_button_if_text_fields_are_not_empty()
            self._activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected()
            if self._help_activated:
                self.help_string = "Help mode disabled!"
        self._root.after(
            1, self._check_if_buttons_should_be_active_or_inactive)

    def _activate_dna_fragment_analysis_buttons_if_dna_fragment_has_been_selected(self):
        if self._dna_fragment_name:
            if self._dna_fragment_name.get() == "None" and self._help_activated == False:
                self.translate_button["state"] = DISABLED
                self.generate_primers_button["state"] = DISABLED
            else:
                self.translate_button["state"] = NORMAL
                self.generate_primers_button["state"] = NORMAL

    def _activate_add_button_if_text_fields_are_not_empty(self):
        if self._name_input:
            if (not Entry.get(self._name_input) or not Entry.get(self.sequence_input)) and self._help_activated == False:
                self.add_button["state"] = DISABLED
            else:
                self.add_button["state"] = NORMAL

    def _add_new_dna_fragment(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["If there are any problems in adding the DNA fragment, you will be notified of it here.", "white"], self.notification_labels)
            self._add_notification(["The added DNA fragments will be stored in a database on your PC hard disk so you can use them also later.", "white"], self.notification_labels)
            self._add_notification(["You cannot add two DNA fragments with the same name. Sequence can contain only natural nucleotides A, T, G and C.", "white"], self.notification_labels)
            self._add_notification(["You can add new DNA fragments here. The button will be activated when you have entered name and sequence.", "white"], self.notification_labels)
        else:
            notification = self._dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(
                Entry.get(self._name_input), Entry.get(self.sequence_input), self._account_service.logged_in_user.name)
            self._add_notification(notification, self.notification_labels)
            self._add_users_dna_fragments_dropdown_list()

    def _translate(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["If there are any problems in generating the protein sequence, you will get notified of it here.", "white"], self.notification_labels)
            self._add_notification(["The protein sequence will be saved to your working directory in 'translations' folder.", "white"], self.notification_labels)
            self._add_notification(["You might find this functionality useful if you want to see how mutations affect the protein sequence.", "white"], self.notification_labels)
            self._add_notification(["Translate button is used to generate the protein sequence the DNA fragment codes for.", "white"], self.notification_labels)
        else:
            dna_fragment = self._dna_fragment_service.get_dna_fragment_by_name_and_owner_name(
                self._dna_fragment_name.get(), self._account_service.logged_in_user.name)
            notification = self._protein_service.attempt_translation_and_return_notification(dna_fragment.name, dna_fragment.for_strand,
                                                                                             self._account_service.logged_in_user.directory)
            self._add_notification(notification, self.notification_labels)

    def _generate_primerss(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["If there are any problems in generating the primers, you will get notified of it here.", "white"], self.notification_labels)
            self._add_notification(["The primers will be saved in your working directory in the 'primers' folder in an Excel file.", "white"], self.notification_labels)
            self._add_notification(["The primers will be by named the name of the DNA fragment, the strand (forward or reverse) and number of the primer.", "white"], self.notification_labels)
            self._add_notification(["You will be able to change these values by clicking 'Settings' from the menu.", "white"], self.notification_labels)
            self._add_notification(["This is done by searching sequences in the strands that have certain length and GC content.", "white"], self.notification_labels)
            self._add_notification(["Generate sequencing primers button is used to generate sequencing primers for both strands of the DNA fragment.", "white"], self.notification_labels)
        else:
            directory = self._account_service.logged_in_user.directory
            primer_length = self._account_service.logged_in_user.primer_length
            primer_gc_content = self._account_service.logged_in_user.primer_gc_content
            dna_fragment = self._dna_fragment_service.get_dna_fragment_by_name_and_owner_name(
                self._dna_fragment_name.get(), self._account_service.logged_in_user.name)
            notification = self._primer_service.attempt_primer_generation_and_return_notification(
                directory, primer_length, primer_gc_content,
                dna_fragment.name, dna_fragment.for_strand, dna_fragment.rev_strand)
            self._add_notification(notification, self.notification_labels)

    def _select_dna_fragment_help(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["You can select DNA fragments that you have added previosly for analysis here.", "white"], self.notification_labels)

    def _settings(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["Opens settings where you can change working directory, sequencing primer length and GC content, or delete your account.", "white"], self.notification_labels)
        else:
            self._account_service.changing_settings = True

    def _exit(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["Click here to exit the application.", "white"], self.notification_labels)
        else:
            self._root.destroy()

    def _logout(self):
        if self._help_activated == True:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(
                ["Click here to logout from the application.", "white"], self.notification_labels)
        else:
            self._account_service.logout()

    def _remove_dna_fragments_and_primers_from_databases_if_account_deleted(self):
        if self._account_service.deleted_account_name:
            for dna_fragment in self._dna_fragment_service.get_all_dna_fragments_by_owner_name(self._account_service.deleted_account_name):
                self._primer_service.delete_all_by_template_dna_name(
                    dna_fragment[0])
                self._dna_fragment_service.delete_by_name(dna_fragment[0])
            self._account_service.deleted_account_name = None
            self._account_service.logged_in_user = None
            self._account_service.changing_settings = False
        self._root.after(1, self._remove_dna_fragments_and_primers_from_databases_if_account_deleted)

    def help(self):
        """A method for activating help mode of the application. In help mode, all buttons and
           menus will generate notifications instead of doing their normal functions. These
           notifications will be displayed in the notification area of the view. If the
           function is called when the help mode is activated, the help mode will be
           inactivated and normal functionalities of the buttons will be resumed.
        """

        if self._help_activated == False:
            self._help_activated = True
            self.help_string = "Help mode disabled!"
            self._dna_fragment_dropdown_menu.destroy()
            self._dna_fragment_dropdown_fake_button = Button(
                self.input_frame, text="None   ", command=self._select_dna_fragment_help)
            self._dna_fragment_dropdown_fake_button.grid(
                row=1, column=1, columnspan=5, sticky=W)
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["To exit help mode, please click 'Help' from the menu again.", "white"], self.notification_labels)
            self._add_notification(["Welcome to help mode! Please click a button to see instructions how to see what it is used for.", "white"], self.notification_labels)
        else:
            self._add_notification(["", "white"], self.notification_labels)
            self._add_notification(["Excellent, now let's get those sequencing primers designed!", "white"], self.notification_labels)
            self.help_string = "Help mode activated!"
            self._dna_fragment_dropdown_fake_button.destroy()
            self._add_users_dna_fragments_dropdown_list()
            self._help_activated = False

    def active(self):
        """A method for activating the view by creating frames and adding all components to them
        """

        if not self.input_frame:
            self._add_frames()
            self._add_analysis_buttons()
            self._add_input_area()
            self._add_users_dna_fragments_dropdown_list()
            self._add_notification_area()
            self._options.delete("Exit")
            self._options.add_command(
                label="Settings", command=self._settings)
            self._options.add_command(label="Logout", command=self._logout)
            self._options.add_command(label="Exit", command=self._exit)

    def inactive(self):
        """A method for inactivating the view by deleting its frames
        """

        if self.input_frame:
            self.input_frame.destroy()
            self._output_frame.destroy()
            self.input_frame = None
            self._output_frame = None
            self._options.delete("Settings")
            self._options.delete("Logout")
            self._options.delete("Exit")
            self._options.add_command(label="Exit", command=self._root.destroy)
