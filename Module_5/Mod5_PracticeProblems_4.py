#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:
r1 = []
for i in range (1, 6):
    for r1f in range(1,6):
        r1.append(r1f * i)
    print(r1)
    r1.clear()