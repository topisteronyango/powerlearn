# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
set1 = set()
set2 = set()

for sets in range(4):
    userInput1 = int(input('Enter elements to set 1: '))
    set1.add(userInput1)

print()
print()

for sets in range(4):
    userInput2 = int(input('Enter elements to set 2: '))
    set2.add(userInput2)

print('Set 1 elements are: ', set1)
print('Set 2 elements are: ', set2)

print()
print()

newSet = set1 & set2
print('Elements that are common in both sets are: ', newSet)


