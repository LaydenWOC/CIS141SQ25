#1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

#creating list 
intlist = []

#making the integer list 0-20
for i in range(21):
    intlist.append(i)

#test range of intlist
#print(intlist)

#filter out odd numbers
for i in range(21):
    if i % 2 == 1:
        intlist.remove(i)

#check filter 
#print(intlist)

#sum
print(sum(intlist))