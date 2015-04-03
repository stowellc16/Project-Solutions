def prime(n):  # finds next prime number until user doesn't want to anymore
    if n == 2:
    	print('2 is the next prime number.')
    	again = input('Would you like to continue? (y/n)')
    else: 
    	for num in range(2, n + 1):
    		if n % num == 0:
    			prime(n + 1)
    		else: 
    			print('%s is the next prime number.' % n)
    			again = input('Would you like to continue? (y/n)')
    if again == 'y':
    	prime(n + 1)
    else:
    	pass


if __name__ == '__main__':
	prime(5)