def factorial(value):
    result = 1
    for n in range(1, value+1):
        result *= n
    print(result)

factorial(5)