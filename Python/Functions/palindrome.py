# uSING A USER DEFINE FUNCTION
def isPalindrome(string):
    if (string ==string[::-1]):
        return "A Palindrome"

    else:
        return "Not a Palindrome"

userInput = input("Enter a string: ")
print(isPalindrome(userInput))

# Using lambda function
isPalindrome = lambda string : "is Palindrome" if string == string[::-1] else "Not a palindrome"
userInput = input("Enter a string: ")
print(isPalindrome(userInput))
