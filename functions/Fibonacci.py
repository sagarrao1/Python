
def fibo(n):
    a=0
    b=1
    # 0 1 1 2 3 5
    if (n==1):
        print(a,end=" ")
    else:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2,n):
            c= a+b
            a,b=b,c
            if c > 100:
                break
            print(c,end=" ")


fibo(20)
