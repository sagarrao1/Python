x=13
for i in range(2, int(x/2)):
    if(x%i==0):
        print(x, 'is Not prime')
        break
else:
    print(x, 'is prime')