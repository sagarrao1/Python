# a=8
# b=9
# print(a+b)
# print(int.__add__(a,b))


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2


    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        s3=Student(m1,m2)
        return s3

    def show(self):
        print(self.m1," ", self.m2)

    def __gt__(self, other):
        n1 = self.m1 + self.m2
        n2 = other.m1 + other.m2
        if n1 > n2:
            print("s1 wins")
        else:
            print("s2 wins")

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1=Student(32,45)
s2=Student(44,2)
s3=s1+s2
# s3.show()
s1.__gt__(s2)

a=9
print(a)
#print(a.__str__())
print(s1)


