__author__ = 'stowellc16'


def main():
    n = int(input("Enter a number: "))
    total = collatz(n)
    print(total)


def collatz(n):  # applies the Collatz Conjecture to a number
    conjected = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
            conjected += 1
        else:
            n = (n * 3 + 1)
            conjected += 1

    return conjected

main()