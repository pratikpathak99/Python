#A store charges $12 per item if you buy less than 10 items. If you buy between
# 10 and 99 items, the cost is $10 per item. If you buy 100 or more items, the cost
# is $7 per item. Write a program that asks the user how many items they are buying and
# prints the total cost.

buy = int(input("how many items they are buying:- "))

if buy < 10:
    charges=str(buy*12)
    print("Your total cost= $"+charges)
elif buy > 10 and buy < 99 :
    charges = str(buy * 10)
    print("Your total cost= $" + charges)
elif buy > 100:
    charges = str(buy * 7)
    print("Your total cost= $" + charges)
