age = int(input("Enter age:"))
if (age >= 18):
    print("You Can Drive")
else :
    print("You can't drive")

# elif and nested if statements
appleprice = int(input("What is the price of Apple"))
budget = 500
if(budget - appleprice >200):
    print("I can buy apple 1kg")
elif(budget - appleprice >100):
    if(budget - appleprice >70):
        print("I can buy apple 500gm")
    elif(budget - appleprice >10):
        print("I can buy apple 100gm")
    else:
        print("I can't buy apple ")

else:
    print("I can't buy apple again")

