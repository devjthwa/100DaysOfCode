# def calcGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)
# a = 9
# b = 8
# calcGmean(a, b)

# # print(gmean)

# c= 7
# d = 6
# calcGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)

def lesser(a,b):
    pass
    # you can use pass to just declare the function
def greater(a,b):
    if a < b:
        print(b, " is greater than ", a)
    elif a == b:
        print(b, " is equal to ", a)
    else:
        print(a, " is greater than ", b)

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
greater(num1, num2)
