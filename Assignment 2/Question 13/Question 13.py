#13.	Replace each element in a list L with its square.

import random
L = []
for i in range(0, 10):
    n = random.randint(1, 10)
    L.append(n)
print(L)
for i in range(0, 10):
    sqr = L[i] * L[i]
    L[i] = sqr
print(L)
