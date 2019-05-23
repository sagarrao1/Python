
def topten():
   n=1

   while(n<=10):
       sq= n*n
       n+=1
       yield sq


vals=topten()
print(vals.__next__())
print(vals.__next__())
for i in vals:
    print(i)