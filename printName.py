                                                                            
import random

#function to print random name in arr.
def findName(arr):
    length = len(arr)

    #generate random number
    index = int(random.random() * length)

    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Raymond Yeung", "Kevin Cao", "Ivan Lam", "Mic\
helle Lo"]
findName(pd1)

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang", ]
findName(pd2)
