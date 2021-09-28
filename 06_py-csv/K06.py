#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-09-28

import csv
import random

#create a dictionary for the csv file
occupations = {}

def select_occupations():
    for key, value in occupations.items():
        random -= value
        if(random <=0):
            print(key)
            break

def main():

    with open('occupations.csv') as csv_file:
        #reads the csv file and splits by the ','
        reader = csv.reader(csv_file, delimiter=',')

        #puts the csv file in a dictionary with the string part as the key
        for row in reader:
            if(row[0] == "Job Class") == False :
                occupations[row[0]] = float (row[1])


    random = random.uniform(0,occupations['Total'])
    del occupations['Total']
    select_occupations()
    
main()
