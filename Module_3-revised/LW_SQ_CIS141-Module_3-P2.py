#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

username = input("Name: ")
userage = int(input("Age: "))
useragenext = userage + 1
output = "\nYour Name is: " + username + "\nAge is: " + str(userage) + "\nAge next year: " + str(useragenext)

print(output)