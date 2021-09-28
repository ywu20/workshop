#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-09-28

import csv
import random

occupations = {}


with open('occupations.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if(row[0] == "Job Class") == False :
            occupations[row[0]] = float (row[1])


random = random.uniform(0,occupations['Total'])
del occupations['Total']
for key, value in occupations.items():
    random -= value
    if(random <=0):
        print(key)
        break
