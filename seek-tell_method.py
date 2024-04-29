# with open('note.txt', 'r') as f:
#     print(type(f))
#     # move 10th byte in the file
#     f.seek(10)
#     # read the next 5 bytes
#     data = f.read(5)
#     print(data) 

#2 2nd program
with open('note2.txt', 'w') as f:
    f.write("Hello Everyone!")
    # f.truncate(5)

with open('note2.txt', 'r') as f:
    print(f.read())