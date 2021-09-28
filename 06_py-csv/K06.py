#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-09-28

import csv
import random

#create a dictionary for the csv file
occupations = {}
tst = {}
def select_occupations(rand):
    for key, value in occupations.items():
        rand -= value
        if(rand <=0):
            return key


def main():

    with open('occupations.csv') as csv_file:
        #reads the csv file and splits by the ','
        reader = csv.reader(csv_file, delimiter=',')

        #puts the csv file in a dictionary with the string part as the key
        for row in reader:
            if(row[0] == "Job Class") == False :
                occupations[row[0]] = float (row[1])


    rand = random.uniform(0,occupations['Total'])
    del occupations['Total']
    return select_occupations(rand)

def test():
    main()
    for i in range(10000):
        a = main()
        try:
            tst[a] +=1
        except:
            tst[a]=1
    print(tst)
test()
