class Student:
    def __init__(self,name, roll):
        self.name=name
        self.roll=roll
        self.lap= self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.comp="Dell"
            self.cpu="i5"
            self.RAM="16 GB"

        def show(self):
            print(self.comp,self.RAM,self.cpu)

s1=Student("Navin",123)
s2=Student("Watson",345)

lap1=s1.lap
lap2=s2.lap
# lap1=Student.Laptop()
# lap2=Student.Laptop()

s2.lap.cpu="i3"
s2.lap.comp="HP"
s2.lap.RAM="8 GB"


s1.show()
s2.show()
# lap1.show()
# lap2.show()