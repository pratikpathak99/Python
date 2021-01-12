#Write a program to print following patterns.
#* * * * *
#* * * *
#* * *
#* *
#*
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15

n = 5
i = 0
while i < n:
    print("* ", end="")
    i += 1
    if i == n:
        print("\n")
        n -= 1
        # print(n)
        i = 0
print("\n")
a = 5
no = 1
for i in range(0, a):
    for j in range(0, i+1):
        print(str(no) + " ", end="")
        no += 1
    print("\n")
