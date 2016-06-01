import numpy as np

primes = np.array([2])

def calculateNextPrime(primes):
    if primes[-1] == 2:
        n = primes[-1] + 1
    else:
        n = primes[-1] + 2

    while True:
        if (n % primes != 0).all():
            primes = np.append(primes, n)
            return primes

        n += 2

n = 600851475143

while primes[-1] <= n:
    if n % primes[-1] == 0:
        n /= primes[-1]
    else:
        primes = calculateNextPrime(primes)

print primes[-1]
