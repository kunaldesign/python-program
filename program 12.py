#program to check leap year.(nest if...else)
y=int(input("year=> "))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print('{} is a leap year.'.format(y))
        else:
            print('{} is not a leap year.'.format(y))
    else:
        print('{} is a leap year.'.format(y))
else:
    print('{} is not a leap year.'.format(y))
exit()
