#program to find profit or loss

#insert data
cost_price=float(input("enter cost price >> "))
selling_price=float(input("enter selling price >> "))

if (selling_price>cost_price):
    #calculate profit
    profit=selling_price-cost_price
    print("you have profit of {}".format(profit))
    
    #calculate profit persentage
    profit_persentage=(profit/cost_price)*100
    print("your profit persentage is {}%".format(profit_persentage))

else:
    #calculate loss
    loss=cost_price-selling_price
    print("you go to loss of {}".format(loss))
    
    #calculate loss persentage
    loss_persentage=(loss/cost_price)*100
    print("your loss persentage is {}%".format(loss_persentage))

#screen stopper
raw_input ("press enter to exit..")
exit()