#Yuqing Wu, Shadman Rakib, Cameron Nelson
#Softdev
#classwork -- print random names fix by collaborating with trio
#2021-09-26
import random

#function to print random name in arr.
def findName(arr):
    length = len(arr)

    #generate random number
    index = random.randint(0,len(arr)-1); #randint is inclusive both sides

    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Raymond Yeung", "Ivan Lam", "Mic\
helle Lo", "Christopher Liu", "Naomi Naranjo", "Ivan Mijacika", "Lucas Lee", "Emma Buller","Renggeng Zheng", "Alejandro\
 Alonso", "Tami Takada", "Yusuf Elsharawy", "Ella Krechmer", "Tina Nguyen", "Shriya Anand","Lucas Tom-Wong", "Angela \
 Zhang","GavinMcGinley"]
findName(pd1)

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang Li", "An\
dy Lin", "Andrew Juang", "Shadman Rakib", "Annabel Zhang","Cameron Nelson", "Eric Guo", "Jonathan Wu", "Noakai \
Aronesty", "Yoonah Chang" "Roshani Shrestha", "Sophie Liu", "Daniel Sooknanan"]
findName(pd2)
