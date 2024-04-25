x =4
print(x)

def hello():
    global x
    x =5
    y = 10
    print(f"local x is {x}")
    print("hello world")
hello()
print(f"the global x is {x}")
x = 2
print(f"the global x is {x}")
hello()
# print(y)