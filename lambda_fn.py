# def double(x):
#     return x*2

# used when single line operation done
double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(5))
print(avg(5,11))

def appl(fx, value):
    return 6 + fx(value)

print(appl(cube,2))