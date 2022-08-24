import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_FEES = "student_fees"
STUDENT_MARK = "student_mark"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_FEES + " TEXT, " + STUDENT_MARK + " INTEGER);")

appLabel = tk.Label(root, text="School Data Base", fg="#ff0000", width=50)
appLabel.config(font=("Sylfaen", 40))
appLabel.grid(row=0, columnspan=2, padx=(40,40), pady=(30, 0))

class Student:
    studentName = ""
    collegeName = ""
    mark = 0
    fees = 0

    def __init__(self, studentName, collegeName, mark, fees):
        self.studentName = studentName
        self.collegeName = collegeName
        self.mark = mark
        self.fees = fees

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
markLabel = tk.Label(root, text="Enter your Total mark", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
feesLabel = tk.Label(root, text="Total fees paid", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 40)
collegeEntry = tk.Entry(root, width = 40)
feesEntry = tk.Entry(root, width = 40)
markEntry = tk.Entry(root, width = 40)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
feesEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
markEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, collegeEntry, feesEntry, markEntry

    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_FEES, STUDENT_MARK
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    fees = feesEntry.get()
    feesEntry .delete(0, tk.END)
    mark = markEntry.get()
    markEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_MARK + ", " +
                       STUDENT_FEES + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       mark + "', " + str(fees) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="fees")
    tree.heading("four", text="mark")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


# def printDetails():
#     for singleItem in list:
#         print("Student name is: %s\nCollege name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.studentName, singleItem.collegeName, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, text="submit", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="view result", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()