# SNAKE, WATER, Gun
# input snake,water or gun option
# if-else statement used

# possiblity
#          s w g
# p1 =    -1 0 1
# comp =s -1 D W L
#     w  0 L D W
#     g  1 W L D


import random
def check(p1, comp):
    if comp == p1:
        return 0
    if (comp == 0 and p1 == 1):
        return -1
    if (comp == 1 and p1 == 2):
        return -1
    if (comp == 2 and p1 == 0):
        return -1

    return 1

comp = random.randint(0,2)
p1 = int(input("Enter a option between snake 0, water 1 and gun 2: "))

print("You: ", p1)
print("Comp: ", comp)
score = check(p1,comp)
if (score == 0):
    print("Draw")
elif score == -1:
    print("You lose the game")
else:
    print("You won")
