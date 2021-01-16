#6.	Write a  function to find the factorial of a given number using recursion.

no = int(input('Enter number = '))
t = 0
def f(x):
    if x == 1:
        return 1
    else:
        t = x * f(x-1)
        return t

r = f(no)
print('factorial = ', r)
