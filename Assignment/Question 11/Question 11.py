#Write a program that prints out a list of the integers from 1 to 20 and their squares. The output should look like this:
#1 --- 1
#2 --- 4
#3 --- 9
#...
#20 --- 400

def printValues():
    for i in range(1, 21):
        p=(i ** 2)
        print(i, "---", p)


printValues()
