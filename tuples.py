tup = (1,2,3,4)
print(type(tup), tup)
# most of similar like list
# tuples are immutable and lists are mutable

city = ("Ahemdabad","Baroda","Junagadh", "Himmatnagar")
temp = list(city)
temp.append("Girnar")
temp.pop(1)
temp[2] = "Dahod"
city = tuple(temp)
print(city)

city1 = ("Ahemdabad","Baroda")
city2 = ("Kolkata", "Delhi")
c = city1 + city2
print(c)

t1 = (0,1,1,1,1,2,3,4)
res = t1.count(1)
print('1 in t1 is',res,'times')