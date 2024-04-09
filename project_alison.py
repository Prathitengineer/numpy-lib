import numpy as np

A = np.array([[1,2],[3,4]])
print("matrix A: ")
print(A)
print("determinant of A:")
print(np.linalg.det(A))

B = np.array([[[1,2],[3,4]],[[1,2],[2,1]],[[1,3],[3,1]]])
print("matrix B: ")
print(B)
print("determinant of B:")
print(np.linalg.det(B))

C = np.array([[2,7],[8,4]])
print("matrix C: ")
print(C)
print("determinant of C:")
print(np.linalg.det(C))

print("det(dot(A,C)): ",np.linalg.det(np.dot(A,C)))
print("det(A)*det(C): ",np.linalg.det(A)*np.linalg.det(C))