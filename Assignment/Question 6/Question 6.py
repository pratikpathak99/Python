#Read the radius of a circle and side of a square from the user using a single input() method.Then calculate and display the area of the
# circle and the square.

PI = 3.14
radius=input("Enter the velue of radius:- ")
side=input("Enter the Value of side:- ")
cir=PI*int(radius)*int(radius)
sq=int(side)*int(side)
print("Area of circle: ",cir)
print("Area of square: ",sq)
