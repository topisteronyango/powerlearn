# #
# Weekly Code Challenge

# Content

# Discussion
# Coding Challenges for basic control flows and functions



# 1. Large Power
# Create a method that tests whether the result of taking the power of one number to another 
# number provides an answer which is greater than 5000. We will use a conditional statement 
# to return True if the result is greater than 5000 or return False if it is not. 
# In order to accomplish this, we will need the following steps:

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False


# Coding Question
# Create a function named large_power() that takes two parameters named base and exponent.

# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    return result
print(large_power(100, 3))





# 2.Divisible By Ten
# Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

# Define the function header to accept one input num
# Calculate the remainder of the input divided by 10 (use modulus)
# Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False


# Coding question
# Create a function called divisible_by_ten() that has one parameter named num.

# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else: 
        return False
print(divisible_by_ten(100))
print(divisible_by_ten(109))

# divisible_by_ten = lambda num : True if num % 10 == 0 False else num % 10 != 0

# print(divisible_by_ten(109))

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)


x = 0
while x < 10:
    x = x + 1
    print(x)


x = 0
for i in range(3):
    x = x + i
    print(x)

z = lambda x : x * x



print(z(6))

n=7
c=0
while(n):
    if(n>5):
        c=c+n-1
        n=n-1
    else:
        break
print(n)
print(c)

str1="hello"

c=0

for x in str1:
    if(x!="l"):

        c=c+1

    else:
        pass

print(c)

str1="hello"

c=0

for x in str1:
    if(x!="l"):

        c=c+1

    else:

        pass
print(c)

for i in range(0,5):

    print(i)

for j in [0,1,2,3,4]:

    print(j)

for k in [0,1,2,3,4,5]:

    print(k)

for l in range(0,5,1):

    print(l)


list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0
for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem
print(sum , end=" ")

