#Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print ”OK;”
# otherwise, print ”Out of range.”

num = float(input("Enter Your Number :- "))

if ((num >= 1)and(num <= 100)):
    print("OK")
else:
    print("Out of range")
