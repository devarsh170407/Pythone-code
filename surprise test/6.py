import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])


firstRow = matrix[0, :]

lastColumn = matrix[:, -1]

print("\nFirst Row:")
print(firstRow)

print("\nLast Column:")
print(lastColumn)
