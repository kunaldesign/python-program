#program to print the fibonacci sequence
nterm=int(input("how many terms?"))
n1=0
n2=1
count=0
if nterm<=0:
    print("please enter a positive integer")
elif nterm==1:
    print("fibonacci sequence upto",nterm,":")
    print(n1)
else:
    print("fibonacci sequence upto",nterm,":")
    while count<nterm:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
raw_input ("press enter to exit..")
exit()