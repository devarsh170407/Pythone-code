import numpy as np
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z = np.array(l1)
print(z)

l2 = [z[1][0],z[1][1]]             #   or l2 = [z[1,0],z[1,1]]
l3 = [z[2][0],z[2][1]]             #   or l3 = [z[2,0],z[2,1]]
n=np.array([[l2,l3]])              #this is for new  matrix 

print(n)

l2 = [z[1,0],z[1,1]]