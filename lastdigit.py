#write a program to print last digit of the number 
number = int(input("enter the number"))
last_digit = number % 10
print(f"last digit of a number{number}:{last_digit}") 
if last_digit % 3 == 0:
    print("last_digit of the number is devisible by 3")
else:
    print("last_digit of the number is not devisible by 3")    