import math

def fibonacci(value):
    a = 1
    b = 2
    _sum = 2
    while True:
        a, b = b, a + b
        if b > value:
            break
        elif b%2 == 0:
            _sum += b
            
    print(_sum)

fibonacci(4000000)
# Run: python3 2.py

