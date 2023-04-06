# Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. Ask the user for input and store 
# the information in the dictionary. Then, print the dictionary to the console.

my_dict = {}

for i in range(1):

    # Step 3: Prompt the user for key and value
    keyname = input("Enter key for name: ")
    valuename = input("Enter value for name: ")

    keyage = input("Enter key for age: ")
    valueage = int(input("Enter value for age: "))
    
    keybook = input("Enter key for favourite book: ")
    valuebook = input("Enter value for favourite book: ")

    # Step 4: Add key and value to dictionary
    my_dict[keyname] = valuename
    my_dict[keyage] = valueage
    my_dict[keybook] = valuebook

print(my_dict)