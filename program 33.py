#program of simple calculator.
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print 'select option.'
print '1.Addition'
print '2.Subtract'
print '3.Multiply'
print '4.Divide'
choice=input('enter choice --> ')
num1=int(input("enter the first number:: "))
num2=int(input("enter the secound number:: "))
if choice == 1:
    print num1,'+',num2,'=',add(num1,num2)
elif choice==2:
    print num1,'-',num2,'=',sub(num1,num2)
elif choice==3:
    print num1,'*',num2,'=',mul(num1,num2)
elif choice==4:
    print num1,'/',num2,'=',div(num1,num2)
else:
    print 'Invalid input!!'
raw_input ("press enter to exit..")
exit()