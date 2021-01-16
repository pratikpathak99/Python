#4.	Write a program that generates a random number between 1 and 10 and prints your name that many times

import random
name = input('Enter your name = ')
x = random.randint(1, 10)
for i in range(0, x):
    print('Random num is = ', x, name)
