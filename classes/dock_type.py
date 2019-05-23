
class Pycharm:
    def execute(self):
        print("compiling")
        print("executing")

class Anaconda:
    def execute(self):
        print("compiling code using Anaconda")
        print("other method")


class Laptop:
    def code(self,ide):
        ide.execute()


# ide=Pycharm()
ide = Anaconda()
lap1=Laptop()
lap1.code(ide)