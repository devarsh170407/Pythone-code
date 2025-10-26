import numpy as np

m = np.arange(1, 10 ,2).reshape(3, 3)


odd_numbers = m[m % 2 == 1]
print("matrix")
print(m)
print("Odd numbers:")
print(odd_numbers)

