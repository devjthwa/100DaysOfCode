'''happy = True
print(happy := False)

number = [1,2,3,4,5]
while (n:= len(number)) > 0:
    print(number.pop())

foods = []
while True:
    food = input("What do you want to eat?")
    if food == "stop":
        break
    foods.append(food)
print(foods)'''

foods = list()
while (food:= input("what food do you like? : ")) != "quit":
    foods.append(food)