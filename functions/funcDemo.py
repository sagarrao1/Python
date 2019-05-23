def greet():
    print('welcome')
    print('Good morning')

def add_sub(a,b):
    c=a+b
    d=a-b
    # print('addition: ',c)
    return c,d

# greet()
result1,result12=add_sub(4,5)
print('add: ',result1,result12)