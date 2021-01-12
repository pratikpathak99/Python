#Write a program that reads number of rows and prints following pattern:
#Input: 6
#  1
#  2    1
#  4    2    1
#  8    4    2    1
# 16    8    4    2     1

num = 6
for i in range(1, num):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")
