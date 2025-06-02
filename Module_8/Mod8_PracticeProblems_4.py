#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas. Write a program that reads the poll.txt file Count how many votes "yea" or "nay" received and print the results.
filename = 'Module_8/poll.txt'

with open(filename) as file_object:
    contents = file_object.read()
    words = contents.split(", ")
    word_count_nay = words.count('nay')
    word_count_yay = words.count('yay')
    print(f"There are {word_count_nay} counts of nay and {word_count_yay} counts of yay.")