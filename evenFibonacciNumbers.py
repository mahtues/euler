a = 1
b = 2

result = 0

while a < 4000000:
    if a % 2 == 0:
        result += a

    c = b + a
    a = b
    b = c

print result
