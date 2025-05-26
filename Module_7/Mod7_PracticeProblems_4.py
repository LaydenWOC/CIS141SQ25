#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:

def ferry_fare(age, vehicle):
    fare = 0
    senior = False
    if age >= 19 and age < 65:
        fare += 10
    if age <= 18:
        fare = 0
        return "free"
    if age >= 65:
        fare += 5
        senior = True
    if vehicle == "True" and senior == False:
        fare += 10
        return fare
    if vehicle == "True":
        fare += 10
        return fare
    return fare

print(ferry_fare(int(input("Age: ")), input("Vehicle True or False: ")))