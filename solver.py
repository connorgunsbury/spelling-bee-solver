# Author: Connor Gunsbury
# This uses dictionaries available at: https://phillipmfeldman.org/English/spelling%20dictionaries.html



d = input("Which dictionary would you like to use? S/M/L")

if d == "S" or "s":
    with open('small.txt', 'r') as dictionary:
        words = [word.rstrip() for word in dictionary]
elif d == "M" or "m":
    with open('small.txt', 'r') as dictionary:
        words = [word.rstrip() for word in dictionary]
    with open('overflow.txt.', 'r') as dictionary2:
        words.append([word.rstrip() for word in dictionary2])
else:
    with open('large.txt', 'r') as dictionary:
        words = [word.rstrip() for word in dictionary]

term = input("What are today's letters? Start with the required letter. ")


words = set(words)
bees = []

for word in words:
    if len(word) < 4:
        continue
    bee = True
    for letter in word:
        if letter not in term:
            bee = False
            break
    if bee == True and term[0] in word:
        bees.append(word)
        
bees.sort()

print(bees)