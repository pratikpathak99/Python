#Write a python program which shows use of math and time module.
import time
print ("Select the Module. \n1.Math Module \n2.Time Module \n")

num=int(input())

if num==1:
    pi=22/7
    degree = float(input("Input degrees: "))
    radian = degree*(pi/180)
    print(radian)
elif num==2:
    localtime = time.asctime(time.localtime(time.time()))
    print ("Local current time :", localtime)
else:
    print("Invalid select..")
