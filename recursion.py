# factorial(7) = 7*6*5*4*3*2*1
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

# function call itself   
# fibonacci series function
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))