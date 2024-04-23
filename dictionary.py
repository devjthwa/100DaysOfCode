# dictionary is ordered collections of data items
dic = {
    "name": "Dev",
    "age": 20,
    "country": "India"
}
print(dic)
print(dic)
print(dic.keys())
print(dic["name"])
print(dic.get("nama")) # check for given key is available or not if available then print and if not then none

for key in dic.keys():
    print(f"The value corresponding of the key {key} is {dic[key]}")

# 2
ep1 = { 101: 2, 102: 4, 105: 6, 108 : 89, 178: 92}
ep2 = { 201: 2, 202: 0, 222: 33}

# ep1.update(ep2)
# ep1.clear()
# empt = {}
# ep1.pop(101)
# ep1.popitem()
# del ep1
del ep1[102]
print(ep1)