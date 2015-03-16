__author__ = 'stowellc16'
# checks if a string is a palindrome


string = input("Enter a string: ")
string = string.lower()  # makes string lowercase
reversed_string = string[::-1]  # reverses the string


if reversed_string == string:
    print('%s is a palindrome.' % string)
else:
    print('%s is not a palindrome.' % string)