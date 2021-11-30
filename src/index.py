import sys
from ui.ui import UserInterface


def main():
    # This will be needed for recursive translation of DNA sequences to protein sequences
    sys.setrecursionlimit(10**6)
    UserInterface()


main()
