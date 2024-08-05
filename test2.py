tax = 0
ar = int(input("enter the price of bike"))
if ar > 100000:
    tax = 15/100*ar
elif pr > 50000 and ar <= 100000:
    tax = 10/100*ar
else:
     tax = 5/100*ar
     print ("tax to be paid",tax)    
