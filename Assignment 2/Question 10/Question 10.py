#10.Write a python program using a function to calculate the super digit of a number.

no = int(input("Enter any number = "))
remain = 0
sum_ = 0
sup = 0
n = no
while no > 0:
    remain = no % 10
    no = no // 10
    sum_ = remain + sum_
print("Sum of digit of", n, "=", sum_)

remain = 0  # resetting remainder
for i in range(0, len(str(sum_))):
    remain = sum_ % 10
    sum_ = sum_ // 10
    sup = remain + sum_
print("Super digit of", n, "=", sup)


