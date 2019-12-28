#program to find HCF & GCD of any number
def computeHCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x % i==0) and (y % i==0)):
            hcf=i
    return hcf
num1=int(input('enter the first number--> '))
num2=int(input('enter the secound number--> '))
print 'The hcf of',num1,'and',num2,'is',computeHCF(num1,num2)
raw_input ("press enter to exit..")
exit()