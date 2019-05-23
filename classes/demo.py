class Computer:

    def __init__(self,cpu,brand):
        print('In init')
        self.cpu=cpu
        self.brand=brand

    def config(self):
        print("Config : ", self.cpu, self.brand)

# a='sagar'
# print(type(a))
comp1=Computer('i5','DELL')
comp2=Computer('i3', 'HP')

# Computer.config(comp1)
# Computer.config(comp2)
print('----------------')
comp1.config()
comp2.config()