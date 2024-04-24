def fn1():
    try:
        l =[1,2,3,5,7]
        i = int(input("Enter"))
        print(l[i])
        return 1
    except :
        print("Error")
        return 0
    finally:
        print("Thanks")

x= fn1()
print(x)