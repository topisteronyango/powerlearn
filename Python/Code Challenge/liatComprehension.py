# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words 
# that have an odd number of characters.

my_list = ['Today', 'is','wonderful', 'than', 'yesterday']


empty_list = []
for word in my_list:
    if len(word) % 2 != 0:
        empty_list.append(word)

print('Original list is: ', my_list)
print('New list is: ', empty_list)