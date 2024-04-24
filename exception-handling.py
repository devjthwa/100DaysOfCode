a= input("enter number : ")
print(f"multiplication of {a} is : ")
try:
    for i in range(1,11):
        print(f"{a} * {i} = {int(a)*i}")
except Exception as e:
    print("sorry not found")

print("some lines of code")
print("end")

try:
    num = int(input("Enter a number"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("You did not enter a number")
except IndexError:
    print("IndexError")