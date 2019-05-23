
a=10

def update():
    #global a
    a=8
    x=globals()['a']
    print(id(x))
    globals()['a']=15
    print('in func:',a)
    print(id(a))

print(a)
print(id(a))
update()
print('outside :',a)
print(id(a))