'''
# 1st
list = [2,3,4,"Dev","Shiv"]
print(list)
print(type(list))
print(list[2])
print(list[-3]) # negative index
print(list[3-3]) #positive index
print(list[1:-1]) 
print(list[0::2]) 


if "Dev" in list:
    print("available")
else:
    print("unavailable")

if "ev" in "dev":
    print("available")
else:
    print("unavailable")
'''
#2nd
l = [11,45,1,1,2,3,4]
print(l)

l.append(7)
print(l)

l.reverse()
print(l)

print(l.count(1))

m = l
m[0] = "Hi"
print(l) # this mean when we change in m list that m is give the reference and do changes in l not in copy of l, it not make copy

# for solution use this
n = l.copy()
n[0] = "hio"
print(l, n)

n.insert(0,"nice")
print(n)

p = [100,200,300]
l.extend(p) #or
j = l+p
print(l)
print(j)