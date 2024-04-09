import numpy as np
n = np.__dict__
n1 = np.array([1, 2, 3, 4])
n2 = np.array([10, 20, 30, 40])
n3 = np.zeros([4, 6])
print(n3)
n4 = np.full([10], 1.1)
print(n4)
n5 = np.arange(1, 8, 7)
print(n5)

n6 = np.shape(n1)
n7 = np.vstack([n1, n2])
n8 = np.hstack([n1, n2])
n9 = np.column_stack(n3)
print(n7,"\n", n8)
