class Computer:
    def __init__(self):
        self.name=""
        self.age=38

    def compare(self,other):
        if (self.age==other.age):
            print(" They are Same Age")
        else:
            print("They are Different")

#Constructor
c1=Computer();
c2=Computer();
#print(id(c1))
c2.name="Sagar"
c1.name="Sanju"
c1.age=29
c1.compare(c2)


print(c1.name)
print(c2.name)

