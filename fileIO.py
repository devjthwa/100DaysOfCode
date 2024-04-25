#1  reading a file
# f = open('myfile.txt','r')
# # f = open('myfile.txt','rt')
# # in text format rb for binary format
# # f = open('myfile2.txt','w')
# # f = open('myfile2.txt','a') # to add lines at last
# text = f.read()
# print(text)
# f.close()

# write file
# f = open('myfile.txt','w')
# f = open('myfile.txt','a')
# f.write("Hello, world!")
# f.close()

# with open('myfile.txt','a') as f:
#     f.write(" Achha Hain")

# ----------------read, readlines
f = open('myfile.txt','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"Marks of student {i} in maths is {m1}")
    print(f"Marks of student {i} in English is {m2}")
    print(f"Marks of student {i} in Science is {m3}")
    print(line)

