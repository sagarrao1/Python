x=int(input('how many candies you want'))
i=1
av=5
while(i<=x):
    if(i>av):
        break
    print('Candy ',i)
    i+=1

print('bye')


for i in range(1,100):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")

print()
print('bye for')


for k in range(1,20):
    if(k%2!=0):
        pass
    else:
        print(k,end=" ")

print()
print('bye pass')