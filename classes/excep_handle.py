a = 9
b = 5

try:
    print("resource open")
    print(a / b)
    k = int(input("Enter number"))
    print(k)

except ZeroDivisionError as e:
    print("this is divide by zero", e)

except ValueError as e:
    print("Input value error: ", e)


except Exception as e:
    print("some other error", e)

finally:
    print("resource closed")

print("Bye")
