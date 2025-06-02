#2. Write a Python program that allows users to log their hiking trips.

filename = "Module_8/hiking_log.txt"
user = ''

while user != '0':
    with open(filename, 'a') as file_object:
        user = input("Hike name and length in miles, 0 to quit: ")
        if user != 0:
            file_object.write(user)