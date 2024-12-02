# This Module has the Functions that allow a User to do Certain Task's

# Importing Required Modules

import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random

from tabulate import tabulate

# Defining the per/km Charge of each Class
sleeper_charge = int(1.5)
third_ac_charge = int(2)
second_ac_charge = int(3)
first_ac_charge = int(4)

# Defining Some Initial Variables
current_date = datetime.date.today()

# A Ticket can be Booked 4 Months before the Actual Trip
max_date = current_date + datetime.timedelta(days=120)


# Functions
def showinfo(cons):
    data=[]
    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="1234", database="railway")
    cur = mn.cursor()
    cur.execute(cons)
    result = cur.fetchall()
    os.system("cls")
    time.sleep(1)
    head = ["Train ID", "Departure Station",
            "Destination Station"]
    if len(result) >= 10:
        try:
            print("Total of", len(result), "Records Found!")
            ask = int(input("Enter the Number of Records you want to See: "))
        except ValueError:
            print("Please Enter a Valid Integer!")
        else:
            #print(head)
            for x in range(ask):
                data.append(result[x])
            table = tabulate(data, headers=head, tablefmt="grid")
            print(table,'\n')
			
    elif len(result) == 0:
        print("No Trains Available!")
    else:
        for x in result:
            data.append(x)
        table = tabulate(data, headers=head, tablefmt="grid")
        print(table,'\n')

    cur.close()
    mn.close()

def AvailableTrains():
    """
    AvailableTrains() -> Shows the List of Available Trains according to the User Requirement

    Parameters -> None   
    
    show all
    filter by destination
    filter by departure station
    """
    ch=int(input("AVAILABLE TRAIN MENU\n0: SHOW ALL\n1: FILTER BY DEPARTURE STATION\n2: FILTER BY DESTINATION\nenter your choice:"))
    if ch==1:
        dp=input("enter departure city (MUMBAI/PUNE/KOLKATA/BANGALORE/DELHI/CHENNAI)\ntype exactly:")
        showinfo("select * from traininfo where DEPARTURE='%s'"%dp)
        pass
    elif ch==2:
        ds=input("enter destination city (MUMBAI/PUNE/KOLKATA/BANGALORE/DELHI/CHENNAI)\ntype exactly:")
        showinfo("select * from traininfo where DESTINATION='%s'"%ds)
        pass
    else:
       showinfo("SELECT * FROM traininfo")
       pass

def CheckFare():
    ss=input("Are you a senior citizen (Y/N):")
    if ss in 'Yy':
       Senior=1
       print("You are a senior citizen confirmed")
    else:
        Senior=2
        print("You are not a senior citizen confirmed")
    c=int(input("which class are you travelling by:\n1 for first\n2 for second\n3 for general\nenter your choice:"))
    if c not in (1,2,3):
        print("enter class correctly (1/2/3)")
        CheckFare()
    else:
        print("\nYour ticket is at a rate of "+str((1500/c)*Senior)+" per person\n")

def ShowBookings():
    """
    ShowBookings() -> Shows the Bookings Made by an User

    Parameters -> None
    """
    data=[]
    mn = mysql.connector.connect(host="localhost", user='root',password='1234', database="railway")
    cur = mn.cursor()

    mobile_no = input("Please Enter your 10 Digit Mobile Number: ")

    cur.execute('SELECT * FROM bookings where Mobile_No="{}"'.format(mobile_no))

    result = cur.fetchall()
    if len(result) == 0:
        print("No Records Found!")
    else:
        booking_no = 1
        head=["Train_No", "Passenger_Name", "Mobile_No",
               "Passenger_Adhaar", "Time_Of_Booking", "Booking_ID", "Class","departure date"]
        for x in result:
            data.append(x)
            booking_no += 1
        table = tabulate(data, headers=head, tablefmt="grid")
        print(table,'\n')

    cur.close()
    mn.close()


def BookTrain():
    """
    BookTrain() -> Let's a User Book a Train

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="1234", database="railway")
    cur = mn.cursor()
    while True:
        try:
            train_no = int(input("Train Number: "))
        except ValueError:
            print("Please Enter a Valid Train Number!")
            continue
        else:
            break

    while True:
        Name = input("Enter your Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 30:
            print("Name too Long!")
        else:
            break

    while True:
        try:
            Mobile = int(input("Enter your Mobile Number: "))
        except ValueError:
            print("Please Enter a Valid Mobile Number!")
            continue
        else:
            if len(str(Mobile)) == 10:
                break
            elif len(str(Mobile)) > 10 or len(str(Mobile)) < 10:
                print("Please Enter a Valid 10 Digit Mobile Number!")
            else:
                print("Please Enter a Valid Phone Number!")

    while True:
        try:
            adhaar = int(input("Enter you Adhaar Number: "))
        except ValueError:
            print("Please Enter a Valid Adhaar Number!")
            continue
        else:
            if len(str(adhaar)) == 12:
                break
            elif len(str(adhaar)) > 12 or len(str(adhaar)) < 12:
                print("Please Enter a Valid 12 Digit Adhaar Number!")
            else:
                print("Please Enter a Valid Adhaar Number!")

    Time_of_Booking = datetime.datetime.now()
    date = Time_of_Booking.date()
    date = date.strftime("%d-%m-%y")
    #date of departure
    while True:
        print("Entering date of departure")
        try:
            year = int(input("Enter Year: "))
        except ValueError:
            print("Please Enter a Valid Year")
            continue
        else:
            if len(str(year)) == 4: #REM add year
                break
            else:
                print("Please Enter a Year")
    while True:     
        try:
            month = int(input("Enter month number: "))
        except ValueError:
            print("Please Enter a Valid month number")
            continue
        else:
            if month <= 12 and month >=1:
                break
            else:
                print("Please Enter a valid month number")

    while True:       
        try:
            mnum = int(input("Enter date of the month: "))
        except ValueError:
            print("Please Enter a date of the month")
            continue
        else:
            if mnum in range(1,32):
                break
            else:
                print("Please Enter a valid month number")
                
    depdate=(str(year)+'-'+str(month)+'-'+str(mnum))

    # Creating Unique ID for each Booking
    id = random.randint(1, 10000)
    cur.execute("SELECT Booking_ID FROM BOOKINGS")
    result = cur.fetchall()
    Used_ID = []
    for x in result:
        for y in x:
            Used_ID.append(y)
    while True:
        if id in Used_ID:
            id = random.randint(1, 10000)
        else:
            break


    classes="1: First\n2: Second\n3: General\n"
    print(classes)
    Class = None
    while True:
        ask = int(input("Please Enter a Class from the one's given above: "))
        if ask == 1:
            Class = "First"
            break
        elif ask == 2:
            Class = "Second"
            break
        elif ask == 3:
            Class = "General"
            break
        else:
            print(classes)
            print("Please Choose an Option from Above!")

    while True:
        q="select departure,destination from traininfo where tid="+str(train_no)
        cur.execute(q)
        res=cur.fetchall()
        print("data entered:")
        table = tabulate([[train_no, Name, Mobile, adhaar, date, Class,depdate,res[0][0],res[0][1]]], headers=['Train ID','Name','Mobile',"Aadhar",'booking date','class','departure date','departure from','destined to'], tablefmt="grid")
        print(table)

        ask = input("Are you Sure you want to Book(Y/N): ")
        if ask in ["Y", "y"]:
            print("Booking...")
            try:
                query = "INSERT INTO bookings values({}, '{}', '{}', '{}', '{}', {}, '{}','{}')".format(train_no, Name, Mobile, adhaar, date, id, Class,depdate)
                cur.execute(query)
            except DataError:
                print("Error in Booking!")
            else:
                table2 = tabulate([[id,train_no, Name, Mobile, adhaar, date, Class,depdate,res[0][0],res[0][1]]], headers=['ticket ID','Train ID','Name','Mobile',"Aadhar",'booking date','class','departure date','departure from','destined to'], tablefmt="grid")
                print(table2,"\nSuccessfully Booked!")
                mn.commit()
                cur.close()
                mn.close()
                break
        else:
            print("Stopping Booking...")
            time.sleep(0.5)
            os.system("cls")
            break


def CancelBooking():
    """
    CancelBooking() -> Allows a User to Cancel Booking

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="1234", database="railway")
    cur = mn.cursor()

    print("Please use the Show my Bookings Option\n to get the Unique ID of the Booking you want to Cancel!")

    while True:
        try:
            unique_id = int(input("Enter the Unique ID: "))
        except ValueError:
            print("Please Enter a Valid ID!")
        else:
            if len(str(unique_id)) == 0:
                print("Invalid ID!")
            elif unique_id < 1:
                print("ID Out of Range!")
            elif unique_id > 10000:
                print("ID Out of Range!")
            elif len(str(unique_id)) != 0 and unique_id >= 1 and unique_id <= 10000:
                cur.execute(
                    "SELECT * FROM bookings WHERE Booking_ID={}".format(unique_id))
                result = cur.fetchall()
                if len(result) == 0:
                    print("No Records Found!")
                    break
                print(["Train_No", "Passenger_Name", "Mobile_No",
                       "Passenger_Adhaar", "Time_Of_Booking", "Booking_ID"])
                for x in result:
                    print(x)
                while True:
                    ask = input("Are you Sure you want to Cancel this(Y/N): ")
                    if ask in ["Y", "y"]:
                        cur.execute(
                            "DELETE FROM bookings WHERE Booking_ID={}".format(unique_id))
                        print("Deleted!")
                        mn.commit()
                        cur.close()
                        mn.close()
                        break
                    elif ask in ["N", "n"]:
                        break
                    else:
                        print("Please Enter either Y (Yes) or N (No)!")
                break
            else:
                print("Please Enter a Valid ID!")
