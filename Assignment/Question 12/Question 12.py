#A course instructor wants to compute overall GPA of a student based on his performance in the whole semester. Maximum GPA is 10. To evaluate a student, the instructor follows the policy as shown below:
#Exam Maximum Marks Weightage
#Quiz 1 20 5%
#Mid Sem 50 20%
#Quiz 2 20 5%
#End Sem 100 30%
#Lab Work 100 20%
#Project 50 20%
#Write a program that reads marks got by a student in all 6 exams and
#based on the policy shown above computes the GPA.Note: Limit the
#float value till two decimal points.

Quiz_One = float(input("Enter Your Marks of Quiz One:- "))
Mid_Sem = float(input("Enter Your Marks of Mid Sem:- "))
Quiz_two = float(input("Enter Your Marks of Quiz Two:- "))
End_Sem = float(input("Enter Your Marks of End Sem:- "))
Lab_work = float(input("Enter Your Marks of Lab work:- "))
project = float(input("Enter Your Marks of Project:- "))

one=float((Quiz_One*5)/20)
two=float((Mid_Sem*2)/50)
three = float((Quiz_two*5)/20)
four = ((End_Sem*30)/100)
five = ((Lab_work*20)/100)
six = ((project*20)/50)

result = one+two+three+four+five+six

print(result)
