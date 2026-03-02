"""class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
d=animal(elephant,65)
print(d.name)"""



"""class gadget:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def range(self):
        print("high")

class oppo:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def range(self):
        print("mid range")

class vivo:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def range(self):
        print("high range")


gad1=gadget("new",2000)
gad2=oppo("newm",5000)
gad3=vivo("neew",8000)

gad1.range()
gad2.range()
gad3.range()"""


"""class mother:
    def family(self):
        print('i am the family member')

class father(mother):
    def family(self):
        print('i am the head of the family')

c=father()
c.family()"""

"""class gogle:
    def add(self,a,b):
        x=a+b
        return x
    def add(self,a,b,c):
        x=a+b-c
        return x
n=gogle()
print(n.add(20,10,5))"""

"""from abc import ABC,abstractmethod

class begin(ABC):
    @abstractmethod
    def first(self):
        pass

class testone(begin):
    def first(self):
        return "first level cmpld"
g=testone()
print(g.first())"""
        

"""from abc import ABC,abstractmethod
class bike(ABC):
    def __init__(self,name):
        self._name=name
    @abstractmethod
    def sound(self):
        pass

    def displayname(self):
        print(f"bikes name:{self.name}")

class hounda(bike):
    def sound(self):
        print("hounda low")

class yamaha(bike):
    def sound(self):
        print("yamaha high")

bikes=[hounda("shine"),yamaha("r15")]
for bike in bikes:
    bike.displayname()
    bike.sound()"""



class gadgets:
    def __init__(self,name,use,price):
        self.name=name
        self._use=use
        self.__price=price
    def showprice(self):
        print(self.__price)
class newgadgets(gadgets):
    def show_use(self):
        print(self.name,self._use)


x=newgadgets("mobile","call",30000)
print(x.name)
x.show_use()

y=gadgets("tablets","game",12000)
print(y.name,y._use)
y.showprice()

    


    


