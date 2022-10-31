from datetime import datetime
from DaySettings import *
from tkinter import Tk

# Use time to determine which setting to encrypt the text with
now = datetime.now()
weekday = now.weekday()

board = Tk()
board.withdraw()

# Creates the decryption dictionaries, prints the start menu
def initialize() -> None:
    generateDecryptions(firstSettings)
    generateDecryptions(secondSettings)
    generateDecryptions(thirdSettings)

    printMenu()

# Prints the start menu
# hello world!!
def printMenu() -> None:
    for i in range(5):
        print(" - ")
    print("Welcome to ISpilledMyLetters!")
    print("Enter E to encrypt some text, and start sending secret messages!")
    print("Enter D to decrypt some secret messages!")
    print("Enter Q to quit")

# Reads user input and performs actions accordingly
def acceptCommands() -> None:
    go = True
    while go:
        answer = input("What do you want to do today?: ")
        if answer == "Q":
            go = False
        elif answer == "E":
            text = input("What would you like to encrypt? ")
            encryptedText = completeEncryption(text, weekday)
            print("Your encrypted word is: " + encryptedText)
            askForClipboard(encryptedText)
        elif answer == "D":
            text = input("What would you like to decrypt? ")
            textToDecrypt = completeDecryption(text)
            print("Turns out it said: " + textToDecrypt)
            askForClipboard(textToDecrypt)
        else:
            print("Sorry, invalid input. Please try again ")


def askForClipboard(message) -> None:
    go = True
    while go:
        answer = input("Would you like to copy to clipboard? Y / N ")
        if answer == "Y":
            board.clipboard_clear()
            board.clipboard_append(message)
            board.update()
            board.destroy()
            print("Copied to clipboard: " + message)
            go = False
        elif answer == "N":
            go = False
        else:
            print("Sorry, invalid input. Please try again ")

def main() -> None:
    initialize()
    acceptCommands()

main()
