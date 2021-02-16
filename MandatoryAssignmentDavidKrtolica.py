# TASK1 - CREATE 3 SETS OF AN ORGANIZATION

boardOfDirs = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

for director in boardOfDirs:
    if not director in employees:
        print(director)

print("\n")

for director in boardOfDirs:
    if director in employees:
        print(director)

print("\n")

count = 0
for person in management:
    if person in boardOfDirs:
        count += 1
        print(count)

print("\n")

for person in management:
    if person in employees:
        print(person)
print("Prints out whole management, meaning it is true.")

print("\n")

for person in management:
    if person in boardOfDirs:
        print(person)

print("\n")

for person in employees:
    if person in management and person in boardOfDirs:
        print(person)

print("\n")

for person in employees:
    if person not in management and person not in boardOfDirs:
        print(person)

print("\n\n")



#TASK 2 - CREATE A LIST OF TUPLES

taskDict = {'a':'Alpha', 'b':'Beta', 'g':'Gamma'}

listOfTuples = [(x) for x in taskDict.items()]
print(listOfTuples)

print("\n\n")



#TASK 3 - SETS TASK

s1 = {'a', 'e', 'i', 'o', 'u', 'y'}
s2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

#UNION
sUnion = s1.union(s2)
print(sUnion)

#SYMMETRIC DIFFERENCE
sSymmetricDiff = s1.symmetric_difference(s2)
print(sSymmetricDiff)

#DIFFERENCE FOR S1 (S1 - S2)
sDiff = s1.difference(s2)
print(sDiff)
print("Returns an empty set beacuse S1 has no different elements comparing to S2 !")

#DISJOINT
sDisjoint = s1.intersection(s2)
print(sDisjoint)

print("\n\n")



# TASK 4 - DATE DECODER

monthDict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

def date_decoder(date):
    took_apart = date.split('-')
    if took_apart[1] in monthDict:
        took_apart[1] = str(monthDict[took_apart[1]])
    took_apart = [int(i) for i in took_apart]
    if took_apart[2] > 21:
        took_apart[2] = took_apart[2] + 1900
    else:
        took_apart[2] = took_apart[2] + 2000
    new_tuple = tuple(took_apart)
    reversed_tuple = new_tuple[::-1]
    print(reversed_tuple)
    
date_decoder('4-MAY-14')