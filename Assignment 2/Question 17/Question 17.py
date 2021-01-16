# 17.	Write a demo program for list comprehension.

import random
L = []
for i in range(0, 10):
    n = random.randint(0, 10)
    L.append(n)
x = [x for x in L if x % 2 == 0]
print('X =', x)

