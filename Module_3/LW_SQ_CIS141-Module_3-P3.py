user_sentence = input("input a sentence: ")
user_word = input("input a word: ") 

sentence_length = len(user_sentence)
new_sentence_length = user_sentence.replace(user_word, "")

print("is word present: ", new_sentence_length == sentence_length)