# # Map
# def cube(x):
#     return x*x*x

# print(cube(2))

# l = [1,2,4,6,4,3]
# # newl = []
# # for i in l :
# #     newl.append(cube(i))
# # print(newl)

# # shorcut way
# newl = list(map(cube,l))
# print(newl)


# # Filter
# def filter_fn(a):
#     return a>3
# newnewl = list(filter(filter_fn,l))
# print(newnewl)

# reduce
from functools import reduce
number = [1,2,3,4,5]
sum = reduce(lambda x,y : x+y, number)
print(sum)