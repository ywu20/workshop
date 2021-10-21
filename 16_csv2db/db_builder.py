#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#creates the tables
command = "create table students (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)
command = "create table courses (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

with open('students.csv') as students:
    student_dict = csv.DictReader(students) # opens the file as a collection of dictionaries

    #add each field to the database
    for i in student_dict:

        command = "insert into students values(?,?,?)" # test SQL stmt in sqlite3 shell, save as string
        c.execute(command, (i['name'], i['age'],i['id']))    # run SQL statement

with open('courses.csv') as courses:
    course_dict = csv.DictReader(courses) # opens the file as a collection of dictionaries

    #add each field to the database
    for i in course_dict:

        command = "insert into courses values(?,?,?)" # test SQL stmt in sqlite3 shell, save as string
        c.execute(command, (i['code'], i['mark'],i['id']))    # run SQL statement
#==========================================================

db.commit() #save changes
db.close()  #close database
