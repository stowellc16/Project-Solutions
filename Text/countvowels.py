__author__ = 'stowellc16'
#  counts the vowels in a string


string = input('Enter a string: ')
list_string = list(string)

vowels = ['a', 'e', 'i', 'o', 'u']
total_vowels = 0  # keeps track of total vowels in a string

for char in list_string:
    if char in vowels:
        total_vowels += 1

if total_vowels > 1:
    print("There are %s vowels in %s." % (total_vowels, string))
elif total_vowels == 1:
    print("There is %s vowel in %s." % (total_vowels, string))
else:
    print("There are no vowels in %s." % string)