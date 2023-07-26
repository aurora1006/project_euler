def multiples3or5():
    sum = 0
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum
    
print(f'Solution is {multiples3or5()}')

#Run: python3 1.py