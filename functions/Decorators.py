def smart_divide(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a

        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b


#print(divide(6,2))
#divide= smart_divide(divide)
print(divide(3,6))