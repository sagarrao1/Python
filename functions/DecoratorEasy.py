def make_pretty(func):
    def inner():
        print('I got Decorated')
        func()
    return inner

@make_pretty
def ordinary():
    print('I am ordinary')

#ordinary()
#ordinary= make_pretty(ordinary)
ordinary()


# function can return another another function
# def is_called():
#     print('is called')
#
#     def is_returned():
#         print('Hello ')
#     return is_returned
#
#     #is_returned()
#
# new= is_called()
# new()

















# function can take another function as argument
#=======================================================================
# def inc(x):
#     return x+1
#
#
# def dec(x):
#     return x-1
#
#
# def operator(func,num):
#      result= func(num)
#      return result
#
#
# print(operator(dec,3))










# def first(msg):
#     print(msg)
#
#
# first('Hello')
# second=first
# del first
# second('Hello from second')
