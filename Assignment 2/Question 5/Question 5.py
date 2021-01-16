#5.	Write a python program using a function to find the sum of digits of a number.

tot = 0
n = int(input('Enter number = '))
for i in range(0, 10):
    t = n % 10
    tot = tot + t
    n = n / 10
print('Sum = ', int(tot))
