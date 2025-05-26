#5. Write a function called level_up(experience) that takes a player's experience
#points and returns their new level based on these rules:

def level_up(experience):
    if experience <= 99:
        return "Level 1"
    if 100 <= experience <= 199:
        return "Level 2"
    if experience >= 200:
        return "level 3"

print(level_up(int(input("Experince Points: "))))