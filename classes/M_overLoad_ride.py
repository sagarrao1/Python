class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    # def sum(self,a=None,b=None,c=None):
    #     s=0
    #     if (a!=None and b!=None and c!=None):
    #         s=(a+b+c)
    #     elif(a!=None and b!=None ):
    #         s=(a+b)
    #     else:
    #         s=a
    #     return s

    def sum(self,a=0,b=0,c=0):
        return a+b+c

    def show(self):
        print(self.m1," ", self.m2)

s1=Student(32,45)
print(s1.sum(5,8,7))
