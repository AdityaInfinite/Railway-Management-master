# This Module has some Other Commonly used Functions

# Importing Required Modules

import os
import time

# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    # Change the path given here to the absolute path of the README file
    with open("..\\..\\Railway-Management-master\\README.txt") as file:
        data = file.read()
        print(data)


def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  WELCOME TO RAILWAY RESERVATION SYSTEM")
        print("1. Show Available Trains")
        print("2. Book a Ticket")
        print("3. Show my Bookings")
        print("4. Cancel a Booking")
        print("5. Check Fares")
        print("6. Clear Screen")
        print("7. Menu")
        print("8. About")
        print("9. Exit")
    else:
        pass
