def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                # temp=list[j+1]
                # list[j+1]=list[j]
                # list[j]=temp

nums=[5,3,6,8,2,4]
sort(nums)
print(nums)