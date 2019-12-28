#program to print decimal to binary conversion using recursion.

def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n % 2)

dec=int(input ('enter decimal digit->>'))
convertToBinary(dec)

raw_input ("press enter to exit..")
exit()