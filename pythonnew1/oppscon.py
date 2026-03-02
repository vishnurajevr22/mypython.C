"""class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printn(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
d=student("joe","duo")
d.printn()"""

"""class division:
    def __init__(self,a,b):
        self.n=a
        self.m=b
    def divide(self):
        return self.n/self.m
class module:
    def __int__(self,a,b):
        self.n=a
        self.k=b
    def mod_divide(self):
        return self.n%self.m
    
class div_mod(division,module):
    def __init__(self,a,b):
        self.n=a
        self.m=b
    def div_and_mod(self):
        divval=division.divide(self)
        modval=module.mod_divide(self)
        return(divval,modval)
x=div_mod(5,5)
print("division:",x.divide())
print("mod_division:",x.mod_divide())
print("divmod",x.div_and_mod())"""
