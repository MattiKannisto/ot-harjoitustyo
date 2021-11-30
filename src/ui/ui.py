from tkinter import filedialog
from tkinter import *
from entities.dna_fragment import DnaFragment
from entities.ribosome import Ribosome
from services.primer_service import PrimerService
from ui.settings import SettingsView


class UserInterface():
    def __init__(self):
        self.ribosome = Ribosome()
        self.dna_fragment = DnaFragment()
        self.primer_service = PrimerService()
        self.primer_length = ""
        self.directory = ""

        self.root = Tk()
        self.root.title("DnaSequencingToolPython")
        self.root.attributes('-zoomed', True)
        self.add_menus()
        self.add_frames()

        self.general_instructions = Label(
            self.input_frame, text="Add new DNA fragment:")
        self.general_instructions.grid(row=0, column=0, columnspan=2, sticky=W)

        self.name_instructions = Label(self.input_frame, text="Name:")
        self.name_instructions.grid(row=1, column=0)
        self.name_input = Entry(self.input_frame)
        self.name_input.grid(row=1, column=1)

        self.sequence_label = Label(self.input_frame, text="Sequence:")
        self.sequence_label.grid(row=1, column=2)
        self.sequence_input = Entry(self.input_frame)
        self.sequence_input.grid(row=1, column=3)

        self.add_button = Button(
            self.input_frame, text="Add", command=self.add)
        self.add_button.grid(row=1, column=4)

        self.add_button = Button(
            self.input_frame, text="Translate", command=self.translate)
        self.add_button.grid(row=1, column=5)

        self.add_button = Button(
            self.input_frame, text="Generate sequencing primers", command=self.generate_sequencing_primers)
        self.add_button.grid(row=1, column=6)

#        self.sequencing_primer_length_dropdown_menu = OptionMenu(
#            self.input_frame, self.primer_length, 10, 20, 21)
#        self.sequencing_primer_length_dropdown_menu.grid(row=5, column=0)

        self.notification_label = Label(self.input_frame, text="")
        self.notification_label.grid(row=2, column=0, columnspan=100, sticky=W)

        self.root.mainloop()

    def add_frames(self):
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=0, columnspan=5, sticky=W+E)

        self.dna_fragment_frame = Frame(self.root)
        self.dna_fragment_frame.grid(row=1, columnspan=10, sticky=W+E)

    def add_menus(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.options = Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options)
#        self.options.add_command(label="Settings", command=self.settings)
        self.options.add_command(label="Exit", command=self.quit)

#    def settings(self):
#        settings_view = SettingsView(self.root)
#        settings_view.grid(row=15, col=0)

    def add(self):
        name = Entry.get(self.name_input)
        sequence = Entry.get(self.sequence_input)
        if name != "" and sequence != "":
            new_dna_fragment = DnaFragment(name, sequence)
            if new_dna_fragment.incorrect_letters_found():
                self.notification_label.config(
                    text="Invalid DNA sequence! The sequence should contain only letters 'A', 'T', 'G' and 'C'")
            else:
                self.dna_fragment = new_dna_fragment
                self.notification_label.config(text=(
                    "DNA fragment '" + new_dna_fragment.get_name() + "' added"))

    def translate(self):
        if self.directory == "":
            self.directory = filedialog.askdirectory()
        if self.dna_fragment.get_sequence() != None:
            translation = self.ribosome.translate(
                self.dna_fragment.get_sequence())
            self.ribosome.write_translation_to_file(self.directory + "/translations", translation)
            self.notification_label.config(text=("Translation of the DNA fragment '" +
                                           self.dna_fragment.get_name() + "' added to folder " + self.directory + "/translations"))

    def generate_sequencing_primers(self):
        if self.directory == "":
            self.directory = filedialog.askdirectory()
        self.primer_service.set_directory_name(self.directory + "/primers")
        if self.dna_fragment.get_sequence() is not None:
            if self.primer_length != '':
                self.primer_service.set_sequencing_primer_length(
                    int(self.primer_length))
            self.primer_service.generate_sequencing_primers(
                self.dna_fragment.get_sequence())
            self.notification_label.config(text=(
                "Sequencing primer file added to the directory '" + self.directory + "/primers" + "'"))

    def quit(self):
        self.root.destroy()
