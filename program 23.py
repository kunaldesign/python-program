#program of multiplication table upto 10.
n=int(input("enter an integer: "))
for i in range(1,11):
    print "%d * %d = %d"%(n,i,n*i)
raw_input ("press enter to exit..")
exit()