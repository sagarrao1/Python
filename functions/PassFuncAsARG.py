def inc(x):
    return x+1


def dec(x):
    return x-1


def operator(func,num):
     result= func(num)
     return result


print(operator(inc,3))
