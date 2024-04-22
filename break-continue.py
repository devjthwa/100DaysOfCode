# for i in range(12):
#     print("8 x", i+1, "=", 8 * (i+1))
#     if (i==10):
#         break
# print("out of loop done")

# continue example
for i in range(12):
    if (i==10):
        print("skip the iteration")
        continue
    print("8 x", i+1, "=", 8 * (i+1))