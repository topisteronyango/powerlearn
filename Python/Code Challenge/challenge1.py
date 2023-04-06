# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.
emptyList = []
count = 0
for num in range(5):
    userInput = int(input("Enter your integer: "))
    emptyList.append(userInput)
    count = count + userInput

print(count)