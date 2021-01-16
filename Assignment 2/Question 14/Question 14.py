# 14.	Count how many items in a list L are greater than 50.

import random
import math
L = []
counter = 0
for i in range(0, 10):
    n = random.randint(10, 100)
    L.append(n)
print(L)
for i in range(0, 10):
    if L[i] > 50:
        counter += 1
print(counter)

