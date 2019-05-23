from array import *

vals= array('i', [12,10,2,6,8,12])
vals= array('i', sorted(vals))
print(vals)
#print(vals.buffer_info())
#vals.reverse()
print(vals)
#print(vals.typecode)
#print(vals.itemsize)
#print(vals.count(1))
#print(vals.index(6))
for i in range(len(vals)):
    #print(vals[i])
    pass
print('another way .......................')
for e in vals:
    #print(e)
    pass

newArr= array(vals.typecode, (a*2 for a in vals))
#print(newArr)


vals.append(0)
print(vals)
print(sorted(vals))
print(vals)


