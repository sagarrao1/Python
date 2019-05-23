class TopTen:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <=10:
            val= self.num
            self.num+=1
            return val
        else:
            raise StopIteration

vals= TopTen()
print(vals.__next__())

for i in vals:
    print(i)














#nums=[7,8,9]
# it= iter(nums)
# print(it.__next__())
# print(next(it))
#
# for i in nums:
#     print(i)