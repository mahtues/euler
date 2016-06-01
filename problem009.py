from math import sqrt

sqrs = [ n**2 for n in range(1,1001) ]

for a2 in sqrs:
    for b2 in sqrs:
        if a2 + b2 in sqrs:
            if sqrt(a2) + sqrt(b2) + sqrt(a2 + b2) == 1000:
                a = sqrt(a2)
                b = sqrt(b2)
                c = sqrt(a2 + b2)
                print a, b, c
                print a + b + c
                print a * b * c
