import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A+B)

print(A-B)

print(A * B)

mat_mul = np.dot(A, B)
print("Matrix Multiplication:\n", mat_mul)

at_mul = A @ B
print("Matrix Multiplication using @ operator:\n", at_mul)

print(A / B)

