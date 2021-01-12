#Write a program that generates and prints 50 random integers, each between 3 and 6

import numpy as np
x = np.random.randint(low=3, high=6, size=50)
print(x)
