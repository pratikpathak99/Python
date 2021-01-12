#Write a python program to print 10*10 multiplication table.

n = 10
no = 1
for i in range(1, 11):
    result = no * n
    print(str(n) + " * " + (str(i)) + " = " + str(result))
    no += 1
