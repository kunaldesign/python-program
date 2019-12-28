#program to display powers of 2 using anonymous function
term=int(input("how many terms ? >> "))
result=list(map(lambda x:2**x,range(term)))
print("the total terms is: %d"%term)
for i in range(term):
    print("2 raised to power %d is %d"%(i,result[i]))
raw_input ("press enter to exit..")
exit()
