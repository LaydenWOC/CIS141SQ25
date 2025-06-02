#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it. Write a Python script that reads a file gardening_tips.txt and prints out each tip one by one.
filename = 'Module_8/gardening_tips.txt'

with open(filename) as gardening_tips:
    for tip in gardening_tips:
        print(tip)