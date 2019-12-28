#compound interest program for banks

#insert value
principle=float(input("enter the principle amount >> "))
rate=float(input("enter the rate (*in only persentage) >> "))
time=float(input("enter the time (*in only year) >> "))

#simple interest
total=float(principle*rate*time)
simple_interest=float (total/100)

#result of simple interest
print("the simple interest is {}".format(simple_interest))

#to find amount
amount=float(principle+simple_interest)
print("total amount is {}".format(amount))
#screen stopper
raw_input ("press enter to exit..")
exit()
