#Write a program to find out list of prime numbers between 1 to number entered by user.

lower = 1
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
