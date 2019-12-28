#program to find the area of triangle
a=float(raw_input("enter the value of a: "))
b=float(raw_input("enter the value of b: "))
c=float(raw_input("enter the value of c: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print "the area of triangle is %f"%area
raw_input("press enter to exit....")
exit()
