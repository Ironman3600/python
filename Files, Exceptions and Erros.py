try:
    a = 3
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Continue with following code")