#Yuqing Wu, Shadman Rakib, Cameron Nelson
#Softdev
#classwork -- print random names fix by collaborating with trio
#2021-09-26

#Summary
#We shared our codes and discussed about which version we should use as the basis of everything. My partners both have unique and interesting addons to their code, but they chose mine code for its simplicity and I modified it and added some more names.
#Discoveries
#I didn't thought about finding the name through reading a file (Which Cameron did) and Shadman puts all the parts that are to be runned in main instead of just putting them in the file.
#Questions
#We didn't have a lot of questions
#Comments
#We added the Shadman's idea about having a main to call everything and only calling the main in the file, but we didn't choose Cameron's reading names from text file because it seems to overcomplicate things. We also put the names into a dictionary.
import random

#function to print random name in arr.
def findName(arr):

    #generate random number
    index = random.randint(0,len(arr)-1); #randint is inclusive both sides

    print(arr[index])

name = {

'pd1' : ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Raymond Yeung", "Ivan Lam", "Michelle Lo", "Christopher Liu", "Naomi Naranjo", "Ivan Mijacika", "Lucas Lee", "Emma Buller","Renggeng Zheng", "Alejandro Alonso", "Tami Takada", "Yusuf Elsharawy", "Ella Krechmer", "Tina Nguyen", "Shriya Anand","Lucas Tom-Wong", "Angela Zhang","Gavin McGinley"],

'pd2' : ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang Li", "Andy Lin", "Andrew Juang", "Shadman Rakib", "Annabel Zhang","Cameron Nelson", "Eric Guo", "Jonathan Wu", "Noakai Aronesty", "Yoonah Chang" "Roshani Shrestha", "Sophie Liu", "Daniel Sooknanan"]
}

def main():
    findName(name['pd1'])
    findName(name['pd2'])

main()
