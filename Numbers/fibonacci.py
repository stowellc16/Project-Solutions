def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
	print(map(fibonacci, range(0, 10)))