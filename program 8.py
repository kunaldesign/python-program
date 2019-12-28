#program of swapping two variable without using temporary variable
x=int(input("enter the x: "))
y=int(input("enter the y: "))
x=x-y
y=x+y
x=y-x
print("the value of x after swapping: {}".format(x))
print("the value of y after swapping: {}".format(y))
exit()
