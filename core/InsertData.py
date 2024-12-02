# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules

import csv
import mysql.connector as con

# Functions


def InsertDataTrain():
    """
    InsertDataTrain() -> Inserts all the Train details in the train_info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="1234",
                     database="railway")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open("C:\\Users\\dalvi_5aqptsx\\Desktop\\Railway-Management-master\\Assets\\Train_details.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO train_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        print("data inserted")
        mn.commit()  # Important: Committing the Changes
        cur.close()
        mn.close()
#InsertDataTrain()


def InsertTrainData():
    """
    InsertDataTrain() -> Inserts all the Train details in the train_info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="1234",
                     database="railway")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open("C:\\Users\\dalvi_5aqptsx\\Desktop\\Railway-Management-master\\Assets\\train.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO traininfo VALUES(%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        print("data inserted!")
        mn.commit()  # Important: Committing the Changes
        cur.close()
        mn.close()
#InsertTrainData()