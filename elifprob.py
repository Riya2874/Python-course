marks = int(input("enter the marks:"))

#if marks are in between 81 - 100
if marks > 80:
    print("very good")
#if marks are between 61 - 80
elif marks>60:
    print("good")
#if marks are between 41 - 60
elif marks>40:
    print("average")
#if marks are below 40
else:
    print("fail")


       