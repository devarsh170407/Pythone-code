import numpy as np

n= np.arange(1, 101)

matrix = n.reshape(10, 10)

print("10x10 Matrix:")
print(matrix)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

p = []
for row in matrix:
    for number in row:
        if is_prime(number):
            p.append(number)

print("\nprime numbers:")
print(p)
