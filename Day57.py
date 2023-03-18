def factorial(value):
    if value == 1:
        return 1
    else:
        return(value * factorial(int(value-1)))
print(factorial(5))