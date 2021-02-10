list = []
vowels = ['a', 'e', 'i', 'o', 'u']

def consonants_alphabetical(s):
    for letter in s:
        if letter not in vowels:
            list.append(letter)
    return list

print(consonants_alphabetical('David'))




l = ['Claus', 'Ibrahim', 'Marko','Perica']
print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=len))
print(sorted(l, key=lambda x: x[-1]))
print(sorted(l, key=lambda x: x.find('a')))

print('\n\n\n')

listOfTuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
print(sorted(listOfTuples, key=lambda x: (x[1], x[0])))