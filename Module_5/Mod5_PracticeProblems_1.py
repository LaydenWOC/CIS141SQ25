#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n =  int(input("Postive number: "))
x = 0
for i in range(n):
    x += i

print("sum total:", x)