#Libarys
import math

#User input
Side_A = float(input("Side A of the Triangle: "))
Side_B = float(input("Side B of the Triangle: "))
Side_C = float(input("Side C of the Triangle: "))

#Heron's formula
Semiperimeter = 1/2 * (Side_A + Side_B + Side_C)
Heron_Area = math.sqrt((Semiperimeter * (Semiperimeter - Side_A) * (Semiperimeter - Side_B) * (Semiperimeter - Side_C)))

#Output
print(f"The area of the Triangle is: {Heron_Area}")