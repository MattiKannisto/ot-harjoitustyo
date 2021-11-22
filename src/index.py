from ui.ui import UserInterface
import sys

def main():
    sys.setrecursionlimit(10**6) # This will be needed for recursive translation of DNA sequences to protein sequences
    userInterface = UserInterface()

main()