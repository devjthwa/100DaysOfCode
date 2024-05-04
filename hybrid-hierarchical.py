# Example of hybrid inheritance
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass
class Derived3(Derived1, Derived2):
    pass

# hyerarchical inheritance

class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass
class D3(Derived1):
    pass
