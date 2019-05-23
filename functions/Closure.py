def making_multiplier_of(n):

    def multiplier(x):
        return n*x

    return multiplier

# Multiplier of 3
times3=making_multiplier_of(3)
#output
print(times3(9))

# Multiplier of 5
times5=making_multiplier_of(5)
#output
print(times5(9))

#output 30

print(times5(times3(2)))
making_multiplier_of.__closure__


# def print_msg(msg):
#
#     def printer(msg1):
#         print(msg+msg1)
#
#     return printer
#     #printer()
#
# print_msg('k')
# another=print_msg("Hello ")
# another('Sagar Rao')
# del print_msg


