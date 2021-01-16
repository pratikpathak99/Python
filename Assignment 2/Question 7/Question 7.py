#7.	Write a function called rectangle that takes two integers m and n as arguments and prints out an m× n box consisting of asterisks. Shown below is the output of rectangle(2,4)
#****
#****

m = 0
n = 0
def test(m, n):
	for i in range(m):
		print('*' * n)
test(2, 4)

