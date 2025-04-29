#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.

user_word = input("word: ")
first_index = int(input("first index: "))
last_index = int(input("last index: "))

print(user_word[first_index:last_index])