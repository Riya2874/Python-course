# if cost price and selling price of an item is input thhrough the keyboard, write a program to determine whether the seller has mad prifit or incurred loss or no prifit no loss. also determine haw much profit he made or loss he incurred.
#solution
cost_price = int(input("enter the cost price:"))
selling_price = int(input("enter the selling price:"))

#if SP is more then CP  -> profit
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("we have made profit of",profit)
#if SP is less then CP -> loss
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("we have incurred loss:",loss)
#if there is no profit no loss 
else:
    print("we have made no profit no loss")
