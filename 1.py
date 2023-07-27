import sys 
import time

def option1(value): # If value = 17

    value = value - 1 # 16

    n1 = value//3 # 5
    n2 = value//5 # 3
    n3 = value//15 # 1

    a = (n1* (n1+1))//2 # 15
    b = (n2 * (n2+1))//2 # 6
    c = (n3 * (n3+1))//2 # 1

    r1 = a*3 
    r2 = b*5 
    r3 = c*15 

    return r1 + r2 - r3 

def option2(m):
    _sum = 0
    for n in range(m):
        if n % 3 == 0 or n % 5 == 0:
            _sum += n
    return _sum


value = int(input().strip())

start_time = time.perf_counter()    
option1 = option1(value)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f'Respuesta: {option1} Tiempo de ejecución: {execution_time}')

start_time1 = time.perf_counter()    
option2 = option2(value)
end_time1 = time.perf_counter()
execution_time1 = end_time1 - start_time1
print(f'Respuesta: {option2} Tiempo de ejecución: {execution_time1}')

value = execution_time < execution_time1

print (f'Opción 1 tiene menor tiempo de ejecución que opción 2: {value}')

#Run: python3 1.py

#Observaciones: 

# Las operaciones matemáticas simples son inherentemente rápidas para la computadora porque están diseñadas para ser ejecutadas en hardware de bajo nivel

# En contraste, los bucles for implican más operaciones y la necesidad de gestionar la iteración y el flujo del programa para cada elemento en la secuencia. Esto conlleva un mayor costo computacional y, por lo tanto, generalmente toma más tiempo en comparación con una operación matemática simple.

#Moraleja: El código puede ser más claro y simple en la segunda opción, pero pueden tener más tiempo de ejecución.