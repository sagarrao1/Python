pos=-1
def search(list,n):
    # i=0
    # while(i < len( list)):
    #     if list[i]==n:
    #         globals()['pos']=i
    #         return True
    #     i+=1
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True


    return False


list=[5,6,3,9,2,13]
n=2
if search(list,n):
    print("Found at ", pos+1)
else:
    print("Not Found")
