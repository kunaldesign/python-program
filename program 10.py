#program using if...else statment to find the largest number
n1=int(input("enter an 1st number: "))
n2=int(input("enter an 2nd number: "))
n3=int(input("enter an 3rd number: "))
if (n1>=n2 and n1>=n3):
    print('{} is the largest number.'.format(n1))
if (n2>=n1 and n2>=n3):
    print('{} is the largest number.'.format(n2))
if (n3>=n1 and n3>=n2):
    print('{} is the largest number.'.format(n3))
exit()
