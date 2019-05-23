from functools import  reduce

seq = [6, 1, 2, 4, 5, 8, 13]

#f= lambda a: a%2==0
#filter
evens= list(filter(lambda a: a%2==0, seq))
print(evens)

#f1= lambda x : x*x
#map
doubles = list(map(lambda x: x*x, evens))
print(doubles)

#reduce
sum = reduce( lambda a,b: a+b, doubles)

print('sum: ',sum)





# def fun1(variable):
#     letters=['a','e','i','o','u']
#     if variable in letters:
#         return True
#     else:
#         return False
#
# sequence=['a','r','t','i','k']
#
# filtered=filter(fun1,sequence)
# print(list(filtered))