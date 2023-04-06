# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.


list_input = []
for i in range(1, 5):

    user_input = int(input("Enter an integer "))
    list_input.append(user_input)
print(list_input)
print(sum(list_input))



# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

my_tuple = ("English", "Maths", "Kiswahili", "Geography", "Computer")
for i in my_tuple:
    print(i)


# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

my_dict = {}
user_name = input("Enter your name\n")
user_age = input("Enter your age\n")
user_fav_color = input("Enter your favourite color\n")

my_dict['Name'] = user_name
my_dict['Age'] = user_age
my_dict['Favorite Color'] = user_fav_color

print(my_dict)


# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

set1 = set()
set2 = set()
for i in range(4):
    user_set1 = int(input("elements of set one: "))
    set1.add(user_set1)

for i in range(4):
    user_set2 = int(input("elements of set two: "))
    set2.add(user_set2)

print(set1)
print(set2)

set3 = set1.intersection(set2)
print(set3)


# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that 
# have an odd number of characters.
word_list = ["Mango", "Orange", "Apple", "Banana", "Strawberry", "Watermellon"]
new_list = [fruit for fruit in word_list if len(fruit) % 2 !=0]
print(new_list)



# These tasks should test your understanding of basic concepts related to lists, tuples, dictionaries, and sets in Python. Good luck