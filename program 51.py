'''python program to check if a number is a strong number.'''

sum=0
num=int(input("enter a number: "))
temp=num
while num:
    i=1
    f=1
    r=num%10
    while i<=r:
        f=f*i
        i=i+1
        sum=sum+f
        num=num//10
if sum==temp:
    print("the number is a strong number.")
else:
    print("the number is not a strong number.")