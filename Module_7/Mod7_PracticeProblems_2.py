#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome (reads the same forward and backward, ignoring case). The function should returns either True or False.

def is_palindrome(user_str):
    user_str_reversed = []
    str_reversed = ""
    #making a reversed list
    for s in user_str:
        user_str_reversed.insert(0, s.lower())
    #translating a list to a string
    for v in user_str_reversed:
        str_reversed += v
    #comparing user string to reversed string
    if str_reversed == user_str.lower():
        print(f"User string: {user_str} is a palindrome.")
    else:
        print(f"User string: {user_str} is not a palindrome.")

is_palindrome(input("input a word: "))