#program to know number is palidrome or not.
rev=0
num=int(input('enter an integer: '))
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num/=10
if(temp==rev):
    print('%d is a palidorme.'%temp)
else:
    print('%d is not a palidrome.'%temp)
raw_input ("press enter to exit..")
exit()