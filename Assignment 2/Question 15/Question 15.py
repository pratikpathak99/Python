#15.	Write a program that generates a list of 20 random numbers between 1 and 100.
#a.	Print the list.
#b.	Print the average of the elements in the list.
#c.	Print the largest and smallest values in the list.
#d.	Print the second largest and second smallest entries in the list
#e.	Print how many even numbers are in the list.

import random

L = []
counter = 0
for i in range(0, 20):
    n = random.randint(1, 100)
    L.append(n)
    
print('List = ', L)

for i in range(0, 20):
    avg = sum(L) / 20
print('Sum =', sum(L))
print('Average = ', avg)
print(max(L))
print(min(L))
counter = 0
for i in range(0, 20):
    if L[i] % 2 == 0:
        counter += 1
print(counter)

