# Perform following functionalities:
#a. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89
#b. Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2
#c. Write a program that uses exactly four for loops to print the sequence of letters below.AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
#d. A program gets 10 numbers from the user and counts how many of those numbers are greater than 10, how many are less then 10.
#e. print Hello a random number of times between 5 and 25.
#f. write a program that generates 10000 random numbers between 1 and 100 and counts how many of them are multiples of 12.
#g. The program asks the user for a number and prints its square, then asks for another number and prints its square, etc. It
#   does this three times and then prints that the loop is done.
#h. The program  will print A, then B, then it will alternate C’s and D’s ﬁve times and then ﬁnish with the letter E once.
#i. If we wanted the above program to print ﬁve C’s followed by ﬁve D’s, instead of alternating C’s and D’s

print("-- Welcome -- \n-- choose any one -- \nA. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89\nb. Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2\nc. Write a program that uses exactly four for loops to print the sequence of letters below.AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG\nd. A program gets 10 numbers from the user and counts how many of those numbers are greater than 10, how many are less then 10.\ne. print Hello a random number of times between 5 and 25.\nf. write a program that generates 10000 random numbers between 1 and 100 and counts how many of them are multiples of 12.")
print("g. The program asks the user for a number and prints its square, then asks for another number and prints its square, etc. It does this three times and then prints that the loop is done.\nh. The program  will print A, then B, then it will alternate C’s and D’s ﬁve times and then ﬁnish with the letter E once.\ni. If we wanted the above program to print ﬁve C’s followed by ﬁve D’s, instead of alternating C’s and D’s")
cho=input("\n-- Please Select Any Alphabet Number -- \n")

if cho == "A" or cho == "a":
    for i in range(8, 90, 3):
        print(i,",",end=" ")

elif cho == "B" or cho == "b":
    for i in range(100, 2, -2):
        print(i,",",end=" ")

elif cho == "C" or cho == "c":
    for i in range(10):
        print("A",end="")
    for i in range(7):
        print("B",end="")
    for i in range(4):
        print("CD",end="")
    for i in range(6):
        print("F",end="")
    print("G",end="")
elif cho == "D" or cho == "d":
    # creating an empty list
    lst = []
    up = []
    down = []
    for i in range(0, 10):
        ele = int(input())
        lst.append(ele)  # adding the element
    for i in range(0,10):
        if(lst[i] <= 10):
            up.append(lst[i])
        else:
            down.append(lst[i])
    print("less then 10 :- ",up)
    print("greater than 10 :- ",down)
