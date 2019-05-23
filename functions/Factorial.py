


def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return(c)

# 1 2 3 4 5

def factR(n):
    if (n==0):
        return 1
    return n*factR(n-1)

result=factR(5)
print(result)