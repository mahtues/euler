n = 1
r = 2

res = 1

for i in range(500):
    res += 4 * n + 10 * r

    n += 4 * r

    r += 2

print res
