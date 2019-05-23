# def update(x):
#     print('before x:',x)
#     print(id(x))
#     x=8
#     print(id(x))
#     print('x: ',x)
#
# a=10
# print(id(a))
# update(a)
# print('a: ',a)

def update(x):
    print('before x:',x)
    print(id(x))
    x[1]=25
    print(id(x))
    print('x: ',x)

lst=[10,20,30]
print(id(lst))
update(lst)
print('lst: ',lst)