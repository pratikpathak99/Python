# Find a minimum of three numbers.
a = float(input("Enter Your Number 1 :- "))
b = float(input("Enter Your Number 2 :- "))
c = float(input("Enter Your Number 3 :- "))

if (a <= b and a <= c):
    print(a, "is the smallest")

elif (b <= a and b <= c):
    print(b, "is the smallest")
else:
    print(c, "is the smallest")
