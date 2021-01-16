#8.	Write a function that takes an integer n and returns a random integer with exactly n digits. For instance, if n is 3, then 125 and 593
# would be valid return values, but 093 would not because that is really 93, which is a two-digit number.

import random
n = int(input('Enter num = '))
r = random.randint(10 ** (n-1), 10 ** n - 1)
print(r)
