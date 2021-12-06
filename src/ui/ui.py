from tkinter import filedialog
from tkinter import *
from entities.dna_fragment import DnaFragment
from entities.ribosome import Ribosome
from services.dna_fragment_service import DnaFragmentService
from services.primer_service import PrimerService
from ui.settings import SettingsView
from ui.login import Login


class UserInterface():
    def __init__(self):
        self.ribosome = Ribosome()
        self.dna_fragment = DnaFragment()
        self.primer_service = PrimerService()
        self.dna_fragment_service = DnaFragmentService()
        self.primer_length = ""
        self.directory = ""
        self.notifications = []
#        self.active_view = None

        self.root = Tk()
        self.root.title("DnaSequencingToolPython")
        self.root.attributes('-zoomed', False)
        self.add_menus()
        self.add_frames()
        self.dna_fragment_name = StringVar(self.input_frame)
        self.dna_fragment_name.set("None")

#        self.general_instructions = Label(
#            self.input_frame, text="Add new DNA fragment:")
#        self.general_instructions.grid(row=0, column=0, columnspan=2, sticky=W)

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
        
        self.translate_button = Button(
            self.input_frame, text="Translate", command=self.translate)
        self.translate_button.grid(row=2, column=0)

        self.generate_primers_button = Button(
            self.input_frame, text="Generate sequencing primers", command=self.generate_sequencing_primers)
        self.generate_primers_button.grid(row=2, column=1)

        self.add_users_dna_fragments_dropdown_list()

#        self.sequencing_primer_length_dropdown_menu = OptionMenu(
#            self.input_frame, self.primer_length, 10, 20, 21)
#        self.sequencing_primer_length_dropdown_menu.grid(row=5, column=0)

        self.notification_labels = []
        for i in range(30):
            self.notification_labels.append(
                Label(self.output_frame, bg='black', fg='white', text=""))
            self.notification_labels[i].grid(
                row=3+i, column=0, columnspan=100, sticky=W)

#      self.active_view = Login(self.root)
        self.root.after(0, self.check_if_buttons_should_be_active_or_inactive)
        self.root.mainloop()

    def add_frames(self):
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=0, columnspan=5, sticky=W+E)

        self.output_frame = Frame(self.root, bg='black', pady=10)
        self.output_frame.grid(row=2, columnspan=10, sticky=W+E)

    def add_menus(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.options = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options)
        self.options.add_command(label="Account settings (NOT FUNCTIONAL YET)")
        self.options.add_command(
            label="Sequencing primer settings (NOT FUNCTIONAL YET)")
        self.options.add_command(label="Exit", command=self.quit)

#    def settings(self):
#        settings_view = SettingsView(self.root)
#        settings_view.grid(row=15, col=0)

    def add_users_dna_fragments_dropdown_list(self):
        self.dna_fragment_being_processed_label = Label(
            self.input_frame, text="")
        self.dna_fragment_being_processed_label.grid(row=1, column=0)
        users_dna_fragments_names = []
        for dna_fragment in self.dna_fragment_service.get_all_dna_fragments():
            users_dna_fragments_names.append(dna_fragment[0])
        if len(users_dna_fragments_names) == 0:
            self.dna_fragment_being_processed_label.config(text="No DNA fragments added")
        else:
            self.dna_fragment_being_processed_label.config(text="Now processing DNA fragment ")
            self.dna_fragment_dropdown_menu = OptionMenu(self.input_frame, self.dna_fragment_name, *users_dna_fragments_names, command=self.select_dna_fragment)
            self.dna_fragment_dropdown_menu.grid(row=1, column=1, columnspan=5, sticky=W)

    def select_dna_fragment(self, name):
        self.dna_fragment = self.dna_fragment_service.get_dna_fragment_by_name(name)

    def add_notification(self, notification):
        self.notifications.insert(0, notification)

    def update_notification_area(self):
        for i in range(len(self.notification_labels)):
            if i < len(self.notifications):
                self.notification_labels[i].config(
                    text=self.notifications[i][0], fg=self.notifications[i][1])

    def add_new_dna_fragment(self):
        name = Entry.get(self.name_input)
        sequence = Entry.get(self.sequence_input)
        notification = self.dna_fragment_service.try_to_create_new_dna_fragment_and_return_notification(name, sequence)
        self.add_notification(notification)
        self.add_users_dna_fragments_dropdown_list()
        self.update_notification_area()

    def check_if_buttons_should_be_active_or_inactive(self):
        self.activate_add_button_if_text_fields_are_not_empty()
        self.activate_dna_fragment_analysis_buttons_if_no_dna_fragment_has_been_selected()
        self.root.after(1, self.check_if_buttons_should_be_active_or_inactive)

    def activate_dna_fragment_analysis_buttons_if_no_dna_fragment_has_been_selected(self):
        if self.dna_fragment_name.get() == "None":
            self.translate_button["state"] = DISABLED
            self.generate_primers_button["state"] = DISABLED
        else:
            self.translate_button["state"] = NORMAL
            self.generate_primers_button["state"] = NORMAL

    def activate_add_button_if_text_fields_are_not_empty(self):
        if not Entry.get(self.name_input) or not Entry.get(self.sequence_input):
            self.add_button["state"] = DISABLED
        else:
            self.add_button["state"] = NORMAL
        
    def translate(self):
        if self.directory == "":
            self.directory = filedialog.askdirectory()
        if self.dna_fragment.get_sequence() != None:
            translation = self.ribosome.translate(
                self.dna_fragment.get_sequence())
            self.ribosome.write_translation_to_file(
                self.directory + "/translations", translation)
            self.notifications.insert(0, ["Translation of the DNA fragment '" + self.dna_fragment.get_name(
            ) + "' added to folder " + self.directory + "/translations", "yellow"])
            self.update_notification_area()

    def generate_sequencing_primers(self):
        if self.directory == "":
            self.directory = filedialog.askdirectory()
        self.primer_service.set_directory_name(self.directory + "/primers")
        if self.dna_fragment.get_sequence() is not None:
            if self.primer_length != '':
                self.primer_service.set_sequencing_primer_length(
                    int(self.primer_length))
            self.primer_service.generate_sequencing_primers(self.dna_fragment)
            self.notifications.insert(
                0, ["Sequencing primer file added to the directory '" + self.directory + "/primers" + "'", "blue"])
            self.update_notification_area()

    def quit(self):
        self.root.destroy()
