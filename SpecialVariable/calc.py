
print("calc module: ",__name__)

def add():
    print('addition',__name__)

def sub():
    print('subtraction')


def welcome():
    print("Welcome to calc module")
    print("you are new user")


def main():
    welcome()
    add()
    sub()

if __name__ == "__main__":
    main()