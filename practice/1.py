''' using index'''

# l1 = [1, 2, 3, 4]
# l2 = [6, 7, 8, 9]

# l1[0], l2[0] = l2[0], l1[0]
# l1[2], l2[2] = l2[2], l1[2]

# print("l1:", l1)
# print("l2:", l2)

'''using slicing'''

# l1 = [1, 2, 3, 4]
# l2 = [6, 7, 8, 9]

# l1[::2], l2[::2] = l2[::2], l1[::2]

# print("l1:", l1)
# print("l2:", l2)

# '''l1 + l2'''

# import numpy as np

# l1 = [1, 2, 3, 4]
# l2 = [6, 7, 8, 9]

# a = np.array(l1)
# b = np.array(l2)

# print (a+b)
# sum(a,b)

# [a + b for a, b in zip(l1, l2)]

l1 = [1, 2, 3, 4]
l2 = [6, 7, 8, 9]

l1.sort()
l2.sort()
print(l1)
print(l2)
print(l1+l2)
print(sum(l1))
print(sum(l2))
print(sum(l1+l2))
