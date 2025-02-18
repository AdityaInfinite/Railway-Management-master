# This is the Main File that loads all the Other Modules

# Importing Required Modules

import core.User_Functions as User
import core.Other as Other
import core.Checks as Check
from time import sleep

# Initial Checks
import core.vars as vars
# Checking the Connection to the MySQL Server
connection_status = Check.CheckConnection()
if connection_status is False:
    quit()
else:
    pass
    #REMCheck.CheckDatabase()  # Checking for the Requirements of the Project

Other.ClearScreen()  # Clear the Terminal Window

# Final Imports

# Ask for the Input and Process it

while True:
    Other.Menu()
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.AvailableTrains()
    elif ans == "2":
        User.BookTrain()
    elif ans == "3":
        User.ShowBookings()
    elif ans == "4":
        User.CancelBooking()
    elif ans == "5":
        User.CheckFare()
    elif ans == "6":
        Other.ClearScreen()
        #Other.Menu()
    elif ans == "7":
        #Other.Menu()
        continue
    elif ans == "8":
        Other.ClearScreen()
        Other.About()
        while True:
            ask = input("enter anything to continue...")
            break
    elif ans == "9":
        print("Closing all Connections..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
