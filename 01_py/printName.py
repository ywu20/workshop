#Yuqing Wu
#Softdev
#classwork -- print random names
#2021-09-22
import random

#function to print random name in arr.
def findName(arr):
    length = len(arr)

    #generate random number
    index = int(random.random() * length)

    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Raymond Yeung", "Ivan Lam", "Mic\
helle Lo"]
findName(pd1)

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang Li"]
findName(pd2)
