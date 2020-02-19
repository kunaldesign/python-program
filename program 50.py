'''python program to check if a number is a prefect number'''

n=int(input("enter any number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+1
if sum==n:
    print("the number is a prefect number.")
else:
    print("the number is not a perfect number.")