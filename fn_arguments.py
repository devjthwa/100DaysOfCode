# learn about default values in functions
def average(a =3,b = 7):
    print("Average is: ", (a+b)/2)

# average(3,3)
# average(b=5)

# def greet(fname, lname):
#     print("Hello, " + fname, lname, "!")

# greet("Ashok","Samrat")

def greet2(**name):
    print("Hello, " + name["fname"], name["lname"], "!")

greet2(fname ="Ashok",lname ="Samrat")

def avg(*num):
    sum = 0
    for i in num:
        sum = sum + i
        return sum / len(num)
        print("Average is ", sum/len(num))
# avg(5,7,9)
c = avg(5,7,9,1)
print(c)
# using return we can store the value of the result in function 
