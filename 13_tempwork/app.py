# Neon Duckies -- Yuqing Wu, Sophie Liu, Hebe Huang
# SoftDev
# K13 - Template for Success
# 2021-10-08



import random
import csv
from flask import Flask, render_template

app = Flask(__name__);
occupations = {}
@app.route("/")
def hello_world():
    return ""

def select_occupations(rand):
    """
    Takes a random number as input, returns the weighted randomly selected occupation

    """
    for key, value in occupations.items():
        #As the dictionary is being looped through, each time the random value generated would subtract
        #the percentage of the occupations. This is kind of like designating areas where the random number
        #can land on and each area would be represented by an occupation.
        rand -= value

        #if the random number is less than 0 after the subtraction, that means it's supposed to land within
        #the area that's represented by this occupation
        if(rand <=0):
            return key


@app.route("/occupyflaskst")
def test_tmplt():
    """
    reads the csv file, renders template and print randomly selcted occupation and
    occupations with different percentages formatted in a table in the template file.

    """
    #choose an occupation with weighted percentage
    with open('data/occupations.csv') as csv_file:
        #reads the csv file and splits by the ','
        reader = csv.reader(csv_file, delimiter=',')
        #puts the csv file in a dictionary with the string part as the key and the percent part as value
        for row in reader:
            if(row[0] == "Job Class") == False :
                occupations[row[0]] = float (row[1])

    #Generate a random double from 0 to 99.8
    rand = random.uniform(0,occupations['Total'])

    #delete 'Total' from dictionary so it will never output 'Total'
    del occupations['Total']

    #select random job
    job = select_occupations(rand)

    return render_template( 'tablified.html', foo="random occupation", random_job = job, collection=occupations)


app.debug = True;
app.run()
