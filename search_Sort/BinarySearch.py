pos=-1
def search(list,n):
    l=0  #lower bound
    u=len(list)-1   # upper bound
    while(l <= u):
        mid =(l+u) // 2  # // it gives int
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                l=mid+1
            else:
                u=mid-1
    return False

list=[5,9,12,34,45,95,121,497,945,1004,5839]
n=10
if search(list,n):
    print("Found at ", pos+1)
else:
    print("Not Found")
