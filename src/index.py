import sys
from tkinter import *
from ui.ui import UserInterface


def main():
    # This will be needed for recursive translation of DNA sequences to protein sequences
    sys.setrecursionlimit(10**6)

    root = Tk()
    root.title("DnaSequencingToolPython")
    root.attributes('-zoomed', False)
    UserInterface(root)
    root.mainloop()


if __name__ == '__main__':
    main()
