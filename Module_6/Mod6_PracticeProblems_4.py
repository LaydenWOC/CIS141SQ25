#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, then print both counts.

#imports
from random import randint

#declares 
intlist = []
negative = 0
positive = 0

#number genarator
for i in range(20):
    intlist.append(randint(-1, 1))

#counter
for x in range(len(intlist)):
    if intlist[x] < 1:
        negative += 1
    else:
        positive += 1

#prints output
print(f"Number of numbers: {len(intlist)} \nNegative = {negative} \nPositive = {positive}")