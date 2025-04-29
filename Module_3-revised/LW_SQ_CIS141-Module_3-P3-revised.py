#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)

user_sentence = input("input a sentence: ")
user_word = input("input a word: ") 



print("is word present: ", user_word in user_sentence )