import sys
from tkinter import *
from ui.ui import UserInterface

MAX_RECURSION_NEEDED_TO_TRANSLATE_DNA_TO_PROTEIN = 10**6

def main():
    sys.setrecursionlimit(MAX_RECURSION_NEEDED_TO_TRANSLATE_DNA_TO_PROTEIN)

    root = Tk()
    root.title("DnaSequencingToolPython")
    root.attributes('-zoomed', False)
    UserInterface(root)
    root.mainloop()


if __name__ == '__main__':
    main()
