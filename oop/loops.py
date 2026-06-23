# factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# print(factorial(6))

# Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# print(fibonacci(20))

# Exponents
def exponential(a, b):
    result = a ** b
    return result

# print(exponential(5, 6)) 

# Avg
def average():
    list = [0, 2, 5, 6, 10]
    result = 0
    avg = 0
    for i in list:
        result += i
    
    avg = result / list.__len__()
    return avg

print(average())


