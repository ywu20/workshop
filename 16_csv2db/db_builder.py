# Team F^2: Michael Borczuk, Yuqing Wu, David Chong
# SoftDev
# K16 -- All About Database
# 2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#creates the tables
command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

with open('students.csv') as students:
    student_dict = csv.DictReader(students) # opens the file as a collection of dictionaries
    #add each field to the database
    for i in student_dict:
        command = "INSERT INTO students VALUES(?,?,?)" # test SQL stmt in sqlite3 shell, save as string
        c.execute(command, (i['name'], i['age'],i['id']))    # run SQL statement

with open('courses.csv') as courses:
    course_dict = csv.DictReader(courses) # opens the file as a collection of dictionaries

    #add each field to the database
    for i in course_dict:

        command = "INSERT INTO courses VALUES(?,?,?)" # test SQL stmt in sqlite3 shell, save as string
        c.execute(command, (i['code'], i['mark'],i['id']))    # run SQL statement


command = "SELECT * FROM students"
c.execute(command)
#c.execute("SELECT * FROM courses")
a= c.fetchall() # it's a list
print(a)
#==========================================================

db.commit() #save changes
db.close()  #close database
