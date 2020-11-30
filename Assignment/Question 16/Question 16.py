#Write a Python program that allows the user to enter exactly twenty floating-point values. The pro- gram then prints the sum,
# average (arithmetic mean), maximum, and minimum of the values entered.
num = []
tot = 0
small  = None
avg = None
big = None
while True:
    numbers = float(input('Enter a positive number, negative to stop: '))
    if numbers < 0:
        break
    tot +=numbers
    num.append(numbers)

if len(num) > 0:
    avg = tot / len( num)
    big = max(num)
    small = min(num)


print('Sum is:', tot)
print('Average is:',avg)
print('Maximum is:',big)
print('Minimum is:',small)
