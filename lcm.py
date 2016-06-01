primes = [ 2, 3, 5, 7, 11, 13, 17, 19 ]
factor = [ 0, 0, 0, 0, 0, 0, 0, 0 ]

for n in range(21):
    for i in range(len(primes)):
        f = 0
        while n > 1 and n % primes[i] == 0:
            n /= primes[i]
            f += 1

        if f > factor[i]:
            factor[i] = f

result = 1
for n in [ pow(p, f) for p, f in zip(primes, factor) ]:
    result *= n

print result

def gcd(a, b):
    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)

    if a < b:
        return gcd(a, b - a)

def lcm(a, b):
    return a * b / gcd(a, b)

def gcd2(a, b):
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        d += 1

    while a != b:
        if a % 2 == 0:
            a /= 2
        elif b % 2 == 0:
            b /= 2
        elif a > b:
            a = (a + b) / 2
        else:
            b = (b - a) / 2

    return a * pow(2, d)

def lcm2(a, b):
    return a * b / gcd2(a, b)

result = 1
for n in range(21):
    result = lcm2(n, result)

print result


