#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:
user = 1
while user != 0:
    user = int(input("Enter a number (0 to stop): "))
    if user != 0:
        print(f"You entered {user}")
print("Exiting...")