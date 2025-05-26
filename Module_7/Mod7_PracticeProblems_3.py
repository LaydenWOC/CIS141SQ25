#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
#For example, water is very effective to fight fire.
#Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
#simple type effectiveness rules. Your solution only needs to work for these three sets of input:

def type_advantage(type1, type2):
    type1 = type1.lower()
    type2 = type2.lower()
    if type1 == "water" and type2 == "fire":
        return "Super effective"
    if type1 == "fire" and type2 == "water":
        return "Not very effective"
    if type1 == "electric" and type2 == "grass":
        return "Neutral"

print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"