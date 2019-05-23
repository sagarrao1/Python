class Car:
    wheels=4

    def __init__(self):
        self.mil=10;
        self.company="Suzuki"

c1=Car()
c2=Car()

c2.mil=9
c2.company="Hyundai"

Car.wheels=5

print(c1.mil, c1.company, c1.wheels)
print(c2.mil, c2.company, c2.wheels)