
def count(lst):
    even=0
    odd=0
    for e in lst:
        if e%2==0:
            even+=1
        else:
            odd+=1

    return even, odd


def find(names):
    for e in names:
        if len(e) >5:
            print(e)

lst=[23,4,5,7,8,9,12]

names=['sagar','raju','vidya sagar','sandhya rani']
find(names)
#e,o=count(lst)
# print(e)
# print(o)
#print("Even : {} and odd : {}".format(e,o))
