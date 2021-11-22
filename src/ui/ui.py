from tkinter import *
from entities.dna_fragment import DnaFragment
from entities.ribosome import Ribosome

class UserInterface():
    def __init__(self):
        self.ribosome = Ribosome()
        self.dna_fragment = DnaFragment()
        
        self.root = Tk()
        self.root.title("DnaSequencingToolPython")
        self.root.attributes('-zoomed', True)
        self.add_menus()
        self.add_frames()        

        self.general_instructions = Label(self.input_frame, text="Add new DNA fragment:")
        self.general_instructions.grid(row=0, column=0, columnspan=2, sticky=W)       

        self.name_instructions = Label(self.input_frame, text="Name:")
        self.name_instructions.grid(row=1, column=0)       
        self.name_input = Entry(self.input_frame)
        self.name_input.grid(row=1, column=1)

        self.sequence_label = Label(self.input_frame, text="Sequence:")
        self.sequence_label.grid(row=1, column=2)
        self.sequence_input = Entry(self.input_frame)
        self.sequence_input.grid(row=1, column=3)

        self.add_button = Button(self.input_frame,text="Add", command=self.add)
        self.add_button.grid(row=1, column=4)

        self.add_button = Button(self.input_frame,text="Translate", command=self.translate)
        self.add_button.grid(row=1, column=5)

        self.dna_fragment_label = Label(self.input_frame, text="")
        self.dna_fragment_label.grid(row=2, column=0, columnspan=100, sticky=W)       

        self.translation_label = Label(self.input_frame, text="")
        self.translation_label.grid(row=3, column=0, columnspan=100, sticky=W)       

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
        self.menu.add_cascade(label="Options", menu = self.options)
        self.options.add_command(label="Exit", command = self.quit)

    def add(self):       
        name = Entry.get(self.name_input)
        sequence = Entry.get(self.sequence_input)
        if name != "" and sequence != "":
            new_dna_fragment = DnaFragment(name, sequence)
            if new_dna_fragment.incorrect_letters_found():
                self.dna_fragment_label.config(text="Invalid DNA sequence!")
            else:
                self.dna_fragment = new_dna_fragment
                self.dna_fragment_label.config(text=("DNA fragment " + new_dna_fragment.get_name() + ": " + new_dna_fragment.get_sequence()))

    def translate(self):
        if self.dna_fragment.get_sequence() != None:
            self.translation_label.config(text=("DNA fragment " + self.dna_fragment.get_name() + " translates to: " + self.ribosome.translate(self.dna_fragment.get_sequence())))

    def quit(self):
        self.root.destroy()