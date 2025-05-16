#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears in the list, and then print the count.

strlist = ["Olympic", "College", "Bremerton", "Palsubo", "Shelton", "Washinton", "Olympic College", "Olympic College is in Washintion"]
olympiccount = 0
checkstr = ''

#checking for 'Olympic' case sensitive
for i in range(len(strlist)):
    checkstr = strlist[i]
    #print(checkstr)
    if checkstr.count('Olympic') != 0:
        olympiccount += 1

#Results
print(f"'Olympic' appaers {olympiccount} times.")
