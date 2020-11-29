#To print digit pattern
#Input : 41325
#Output :
#|*****
#|**
#|***
#|*
#|****

def pattern(n):
	for i in n:
		print("|", end = "")
		print("*" * int(i))
n = "41325"
pattern(n)
