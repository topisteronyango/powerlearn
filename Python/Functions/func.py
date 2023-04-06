# def names(*namess):
#     # using list comprehension
#     empty_list = [nam for nam in namess]

#     # Using for loop
#     # empty_list = []
#     # for nam in namess:
#     #     # print(nam)
#     #     empty_list.append(nam)

#     return empty_list

# naming = names("Topister", "Onyango", "Nandera", "Bety")
# print(naming)

# def sum(*num):
#     count = 0
#     for i in num:
#         count += i

#     print(count)
#     return count

# total = sum(20, 40, 50)

# You can use **kwargs in Python to add integers in a function by accepting 
# variable keyword arguments and then using a loop to add all the integer values 
# passed in the arguments. Here's an example function that does this:
# In this function, **kwargs allows you to accept an arbitrary number of keyword arguments. 
# Then, the function loops through each key-value pair in the kwargs dictionary and checks
# if the value is an integer. If it is, it adds it to the result variable. Finally, 
# the function returns the total sum of all the integer values.
# Here, num1, num2, and num3 are the keyword arguments passed to the function. 
# They can have any name, as long as they are preceded by the double-asterisk (**) 
# syntax to indicate that they are keyword arguments.

# isinstance() is used to ensure that only integer values are added together. 
# This is because kwargs can contain arguments of different data types, and attempting to 
# add together values that are not integers would result in a TypeError.















def add_integers(**kwargs):
    result = 0
    for key, value in kwargs.items():
        if isinstance(value, int):
            result += value
    return result
print(add_integers(num1=10, num2=50, num3=30))

# def add_ages(**ages):
#     sum_total = 0
#     for k, v in ages.items():
#         sum_total = sum_total + v
#         print(sum_total)
#         return sum_total

# print(add_ages(topister=30, nandera=45, Bety= 60))
# print(Ages)