import numpy as np

n = np.array(range(100,1000)).reshape(len(range(100,1000)), 1)

prod = n * n.T

prod = prod.reshape(prod.shape[0] * prod.shape[1])
prod.sort()

for n in prod[::-1]:
    if str(n) == str(n)[::-1]:
        print n
        break
