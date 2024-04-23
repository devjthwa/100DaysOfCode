# sets is a collection of well-defined obj
dev = {}
dev2 = set()
print(type(dev)) # dictionary
print(type(dev2)) # set


s1 = {1,2,3,4,5,"Dev"}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.difference(s2))
print(s1.difference_update(s2))
print(s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))
print(s1.add(10))
print(s1.remove(1))
print(s1.discard(1))
print(s1.pop())
print(s1.clear())
print(s1.copy())