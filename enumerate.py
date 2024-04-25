marks = [12,56,38,67,78,1,4]

index = 0
for mark in marks:
    print(mark)
    if (index == 4):
        print("Wah!")
    index +=1
marks = [12,56,38,67,78,1,4]

#  2nd way using
for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 4):
        print("Wah!")
