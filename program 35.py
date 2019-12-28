#program to display calendar of given month of the year.
import calendar

yy=int(input('enter year--> '))
mm=int(input('enter month--> '))

print (calendar.month(yy,mm))

raw_input ("press enter to exit..")
exit()