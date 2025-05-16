#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

#Declears
intlist =  [2, 4, 16, 256]

#Unmodified
print("unmodified", intlist)

#Squering
for i in range(len(intlist)):
    intlist[i] = intlist[i] ** 2

print("squared", intlist)