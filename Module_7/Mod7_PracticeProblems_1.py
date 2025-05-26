#1. Write a function called count_vowels(input) that takes a string and returns the number of vowels (a, e, i, o, u) in it.

def count_vowels(user_str):
    total = 0
    for s in user_str:
        if s.lower() == "a" or "e" or "i" or "o" or "u":
            total += 1
    print(f"Total number of vowels: {total}")

count_vowels(input("Input a string: "))
