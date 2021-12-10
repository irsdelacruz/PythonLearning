import math as m

# basic primality test with reduced search space

def prime_checker(n):
    for i in range(2,m.floor(m.sqrt(n))):
            print(f"Checking for {i}")
            if n % i == 0:
                return False
    return True

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        print(f"Checking for {i}")
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    n = int(input("Check this number: "))
    print(f"{n} is a prime? {is_prime(n)}")
