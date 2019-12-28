#program using if...else statment to find the largest number
n1=int(input("enter an 1st number: "))
n2=int(input("enter an 2nd number: "))
n3=int(input("enter an 3rd number: "))
if (n1>=n2):
    if(n1>=n3):
        print('{} is the largest.'.format(n1))
    else:
        print('{} is the largest.'.format(n3))
else:
    if(n2>=n3):
        print('{} is the largest.'.format(n2))
    else:
        print('{} is the largest.'.format(n3))
exit()

