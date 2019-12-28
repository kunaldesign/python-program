#program to read marks and print percentage and division
print 'enter the subject marks:'
maths = float(input("maths => "))
hindi = float(input("hindi => "))
sanskrit = float(input("sanskrit => "))
science = float(input("science => "))
social = float(input("social => "))
english = float(input("english => "))
total = maths+hindi+sanskrit+science+social+english
per = float(total)*100/600
print("total marks: %d" % (total))
print ("percentage is: %f" % (per))
if per>=60:
    print "first division"
elif per>=40:
    print "secound division"
else:
    print "fail"
raw_input ("press enter to exit..")
exit()