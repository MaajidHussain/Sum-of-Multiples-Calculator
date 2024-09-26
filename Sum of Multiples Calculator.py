def Sum(Number,Count):
    total=0
    if Number==0:
        return 0
    for i in range(1,Count+1):
        total=total+i*Number
    return total
try:
    Number=int(input("Enter an integer: "))
    Count=int(input("Enter the number of Multiples to sum: "))
    result=Sum(Number,Count)
    print(result)
except:
    print("Please enter a valid input integer.")