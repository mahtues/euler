from numpy import array, append

primes = array([2, 3])

while primes.shape[0] < 10001:
    n = primes[-1] + 2

    while (n % primes == 0).any():
        n += 2

    primes = append(primes, n)

print primes[-1]
