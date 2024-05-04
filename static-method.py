class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
    @staticmethod # using staticmethod without using self 
    def add(x, y):
        return x + y

result = Math.add(1,2)
print(result)

a= Math(5)
print(a.num)
a.addtonum(6)
print(a.num)