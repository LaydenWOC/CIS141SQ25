#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

#declarments
strlist = ["Olympic"]
strsource = strlist[0]
check = False

#Genrates a list from the input string
for char in range(len(strlist[0])+1):
    strlist.append(strsource[0:char])

#removes first instance of the seed word
strlist.pop(0)

#sorts by length
strlist.sort(key=len)

#pops items less then 3 chars in length
while check != True:
    for i in range(len(strlist)+1):
        if len(strlist[0]) <= 3:
            strlist.pop(0)
    check = True

#prints resulting list
print(strlist)