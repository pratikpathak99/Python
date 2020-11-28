#Given an integer day , where 1≤𝑑𝑎𝑦≤7, print Weekday,  if the day corresponds to weekday, print Weekend otherwise.
#1, 7: Weekend
#2,3,4,5,6: Weekday

a = [1,2,3,4,5,6,7]
weekend=[]
Weekday=[]

for x in a:
  if x == 1:
      weekend.append(x)
  elif x == 7:
      weekend.append(x)
  else:
      Weekday.append(x)

print(weekend," : Weekend")
print(Weekday," : Weekday")

