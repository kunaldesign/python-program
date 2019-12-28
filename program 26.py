#program to print reverse number by the giving number.
rev = 0
num = int(input('enter an integer: '))
while(num > 0):
    rem = num % 10
    rev = rev*10+rem
    num /= 10
print rev
raw_input ("press enter to exit..")
exit()