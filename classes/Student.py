class Student:
    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is independent method")

s1=Student(23,45,42)
s2=Student(22,45,68)

print(s2.avg())

print(s1.get_m1())

s1.set_m1(99)

print(s1.m1,s1.m2,s1.m3)
print(s2.m1,s2.m2,s2.m3)

print(Student.getSchool())
Student.info()