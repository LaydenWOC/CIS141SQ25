#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = input()

G = False
PG13 = False
R = False

if int(age) < 13:
    G = True
elif int(age) >= 13 and int(age) <= 17:
    G = True
    PG13 = True
elif int(age) >= 18:
    G = True
    PG13 = True
    R = True

print(f"You can view: \nG: {G} \nPG-13: {PG13} \nR: {R}")