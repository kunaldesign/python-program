#program to check armstrong number
num=int(input("enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("%d is an armstrong number"%num)
else:
    print("%d is not an armstrong number"%num)
raw_input ("press enter to exit..")
exit()