import numpy as np

# Create the 5x5 matrix directly from a list of lists.
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])


top_row = matrix[0, :]

bottom_row = matrix[-1, :]

left_column = matrix[1:-1, 0]

right_column = matrix[1:-1, -1]


border_elements = np.concatenate((top_row, bottom_row, left_column, right_column))

print("\nextracted elements:")
print(border_elements)
