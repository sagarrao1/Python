f= open('Mydata','r')
f1=open('abc','w')
#f1=open('abc','a')

f2=open('IMG_4094.JPG','rb')
f3=open('MyPic.JPG','wb')
# print(f)
#print(f.readline())
# f1.write("  This is test write\n")
# f1.write(" this second line")
#f1.write("\n this is append\n")

#Write from Mydata to abc
for data in f:
    f1.write(data)

#read jpg and write to another file
for data in f2:
    f3.write(data)

