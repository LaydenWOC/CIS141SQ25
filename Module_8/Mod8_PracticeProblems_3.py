#3 Create a text file called song_lyrics.txt and copy the lyrics of a song in to it. Requests 5 inputs from the user: 5 words the user would like to count the frequency of
filename = 'Module_8/song_lyrics.txt'

with open(filename) as file_object:
    contents = file_object.read()
    words = contents.split()
    user_word =  input("Choose a word: ")
    word_count = words.count(user_word)
    print(f"There are {word_count} instances of '{user_word}'.\nP.S. Case senstive.")