#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06 -- StI/O: Divine your Destiny!
#2021-09-28

#Discoveries:
#Although we didn't use it in our code, we discovered random.choice which can be used for weighted randomness.
#How to use csv to read files and split it with csv.reader.
#Refamiliarize myself with how to do things with the dictionary.
#The first time we thought about the algorithm we were thinking of accumulating the percentage to make each number
#range represent an occupation. However, that would require extra work to indicate which section belongs to which
#occupation. Sometimes, subtration can be a lot neater than addition.

import csv
import random

#create a dictionary for the csv file
occupations = {}
tst = {}

keys = []
#choose an occupation with weighted percentage
def select_occupations(rand):
    for key, value in occupations.items():
        #As the dictionary is being looped through, each time the random value generated would subtract
        #the percentage of the occupations. This is kind of like designating areas where the random number
        #can land on and each area would be represented by an occupation.
        rand -= value

        #if the random number is less than 0 after the subtraction, that means it's supposed to land within
        #the area that's represented by this occupation
        if(rand <=0):
            return key


def main():

    with open('occupations.csv') as csv_file:
        #reads the csv file and splits by the ','
        reader = csv.reader(csv_file, delimiter=',')
        #puts the csv file in a dictionary with the string part as the key and the percent part as value
        for row in reader:
            if(row[0] == "Job Class") == False :
                occupations[row[0]] = float (row[1])
                keys.append(row[0])

    #Generate a random double from 0 to 99.8
    rand = random.uniform(0,occupations['Total'])

    #delete 'Total' from dictionary so it will never output 'Total'
    del occupations['Total']
    keys.remove('Total')

    #return the occupation chosen with weighted percentage
    return select_occupations(rand)

#a very simple tester
def test():
    #testing the distribution for running the program 10000 times
    for i in range(10000):
        #calls main()
        a = main()

        try:
            # if the key is never called, this line would fail, otherwise add to the number of times the key gets returned.
            tst[a] +=1
        except:
            #the key for that occupation is created and that counts as being generated once.
            tst[a]=1
    print(tst)

#print(main())
