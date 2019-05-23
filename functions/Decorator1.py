def smart_divide(func):
    def inner(a,b):
        print("The value of dive are ", a, " and ", b)
        if (b==0):
            print('Can not divide by zero')
            return
        return func(a,b)
    return inner

#@smart_divide
def divide(a,b):
    return a/b

#print(divide(4,2))
divide= smart_divide(divide)

print(divide(4,0))