__author__ = 'stowellc16'
# counts words in a string


string = input('Enter a string: ')

# splits the string at every word
numwords = len(string.split(' '))

print('The string contains %s words.' % numwords)

